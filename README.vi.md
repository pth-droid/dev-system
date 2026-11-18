# Dev System v4.8.1

Bản này thay thế bộ v3 và bản 4.0 (xem [CHANGELOG.md](CHANGELOG.md)). Giữ hai skill phương pháp: `dev-guardrails`
và `release-housekeeping`. Phân loại scope, giao việc và ba tier vẫn nằm
trong workflow, không nằm trong skill dev.

## Nhìn nhanh: quy trình giúp gì

Bạn nói nhu cầu và quyết các câu hỏi nghiệp vụ. Agent lo phần còn lại, và mỗi
chặng có một điểm dừng để lỗi không đi tiếp sang chặng sau.

```mermaid
flowchart TD
    A["Bạn nói nhu cầu<br/>/dev ..."] --> B{"Agent phân loại<br/>theo việc, không theo lời"}
    B -->|"Sửa chữ, sửa nhỏ đã rõ"| Q["QUICK_FIX<br/>phiên rẻ làm, báo về"]
    B -->|"Một tính năng hoặc một lỗi"| S["STANDARD"]
    B -->|"Việc lớn nhiều mốc"| L["LARGE<br/>chia mốc, làm mốc đã duyệt"]
    L --> S
    S --> D["Khảo sát và đo<br/>máy chủ đang chạy gì, số liệu thật"]
    D --> E["Bạn quyết<br/>thẻ quyết định bằng lời thường"]
    E --> F["Builder viết test trước,<br/>rồi viết mã, commit cục bộ"]
    F --> G["Lead soát<br/>bằng chứng, diff, trạng thái cuối"]
    G -->|"Có lỗi"| F
    Q --> H
    G -->|"Đạt"| H["Bạn bấm thử<br/>các bước kèm ảnh chụp"]
    H -->|"Chưa ổn"| F
    H -->|"OK"| I["READY_FOR_PR"]
    I -->|"Bạn nói: ship đi"| J["PR, gộp, triển khai,<br/>kiểm trên máy chủ"]
    J --> K["Dọn nhánh, worktree,<br/>môi trường thử"]
```

Nếu sơ đồ không hiện: nhu cầu → phân loại → khảo sát và đo → bạn quyết →
test trước rồi mã → lead soát → bạn bấm thử → READY_FOR_PR → "ship đi" →
triển khai và kiểm → dọn dẹp.

| Điểm dừng | Nó chặn loại lỗi nào | Ví dụ từ lượt chạy thật trên LH-ERP |
| --- | --- | --- |
| Khảo sát và đo | Quyết định dựa trên giả định | Ngưỡng so chữ giả định 0,70, đo ra phải là 0,30 |
| Bạn quyết | Agent tự chọn thay bạn về nghiệp vụ | 8 quyết định của một thay đổi được ghi lại kèm phương án đã bỏ |
| Test trước rồi mã | Mã chạy được nhưng sai yêu cầu | Lỗi được tái hiện bằng test trước khi sửa |
| Lead soát | Báo "đạt" nhưng kết quả sai | Test đạt 60/60 trong khi đơn vị bị đổi từ Hộp sang ml |
| Bạn bấm thử | Đúng theo test nhưng khó dùng | Phần dưới của cửa sổ soát được làm lại sau khi bạn xem |
| Kiểm trên máy chủ | Script báo thành công nhưng thiếu thứ gì đó | Triển khai báo xong trong khi thiếu một model |
| Dọn dẹp | Nhánh, container, tệp tạm tồn lại | Giữ volume, xoá phần còn lại, hỏi bạn một lần |

Quyền của bạn nằm ở ba chỗ: quyết nghiệp vụ, bấm thử, và nói "ship đi".
Agent không đẩy mã, không gộp và không triển khai khi chưa có câu đó.

## Cài bằng agent

Đọc [INSTALL-HANDOFF.md](INSTALL-HANDOFF.md), hoặc giao file tự chứa
`INSTALL-DEV-SYSTEM.md` được cung cấp riêng. File tự chứa có cả bộ cài;
đặt ở thư mục bất kỳ và chỉ rõ repo đích. Giữ cấu hình riêng cũ,
cài trong worktree setup riêng; chưa commit/push/merge/deploy hoặc dọn Docker.

## Một lệnh để bắt đầu

- Claude Code: `/dev <nhu cầu>` sau khi cài adapter đúng.
- Codex: `$dev <nhu cầu>` hoặc bộ chọn skill thực tế.
- Host tự xây: cần binding `/dev` thực sự, không chỉ viết trong Markdown.

Adapter chỉ trỏ đến [dev-router.md](workflow/dev-router.md); không sao chép
quy tắc routing hay tạo một hệ thống agent mới.

| Luồng | Cách làm |
| --- | --- |
| QUICK_FIX | Sửa chữ, docs, khoảng cách (không đổi logic): nhánh ngắn, commit message, một check. Sửa hành vi nhỏ, rõ và ít rủi ro: ghi yêu cầu ngắn, TDD/check phù hợp, review gọn. |
| STANDARD | Một feature hoặc bug cần điều tra: spec gọn, vertical tasks, main review và cùng builder fix. |
| LARGE | Lập hướng tổng thể, chia mốc và chỉ build mốc được duyệt cho phiên hiện tại. |

Scope, rủi ro và tier là các trục khác nhau. Sửa một dòng phân quyền
không phải quick fix ít rủi ro. Agent tự phân luồng và nêu lý do;
chỉ hỏi bạn các quyết định có ảnh hưởng thực sự.

Mọi change dùng worktree riêng, trừ sửa chữ/docs/khoảng cách trong QUICK_FIX
(chỉ cần nhánh ngắn). Tất cả luồng vẫn cần bằng chứng thật, TDD khi sửa hành vi
và gate trước PR.

- Commit: agent được commit cục bộ trên nhánh của change. Push, PR, merge và
  deploy vẫn cần quyền riêng.
- Song song: các change không đụng nhau được chạy song song, mỗi change một
  worktree; agent báo cho bạn biết change nào chạy song song và vì sao.
- Xem tận mắt: với thay đổi bạn nhìn thấy hoặc dùng được, agent đưa các bước
  bấm thử kèm ảnh chụp và chờ bạn OK trước READY_FOR_PR.
Đọc [daily-workflow.md](workflow/daily-workflow.md) và [prompts.md](workflow/prompts.md).

## Trong lúc builder làm, và lúc soát

- **Builder yếu hơn thì hỏi lead.** Giao việc cho tác tử con Claude luôn theo `/dev`. Builder
  dùng model thấp hơn lead thì gặp quyết định hay điều chưa chắc mà spec chưa trả lời phải nhắn
  lead trước khi làm tiếp: bối cảnh, câu hỏi, các phương án, đề xuất, dưới 400 từ.
- **Theo dõi theo sự kiện.** Phần tốn của mỗi lần kiểm tiến độ là lead đọc lại cả cuộc trò
  chuyện. Với builder Codex, script `tools/watch-codex-job.sh` tự kiểm mỗi 5 phút, không tốn
  token, và chỉ đánh thức lead khi có commit mới, job xong hoặc lỗi, lỗi hạn mức, hoặc sau 40
  phút (vừa kiểm treo vừa giữ ấm bộ nhớ đệm). Tác tử con Claude không cần script: nó tự nhắn lead.
- **Báo có nguồn.** Mỗi câu tiến độ ghi rõ nguồn ("nhật ký builder ghi …", "commit …") và đánh
  dấu phần lead chưa tự kiểm.
- **Soát bằng cách kiểm độc lập.** Chạy lại test của builder chỉ chứng minh bằng chứng có thật.
  Việc có số liệu: (a) đối chiếu số tổng bằng cách tính riêng, mọi chênh lệch giải thích tới
  từng đơn vị, và (b) đọc assertion so với tiêu chí chấp nhận. Quy tắc then chốt: (c) cố tình làm
  hỏng quy tắc trên bản nháp, test phải đỏ. Lead đọc toàn bộ nhật ký tiến độ một lần và so với
  báo cáo cuối.

## Giữ môi trường test tái sử dụng

Dọn dữ liệu của lượt test, không xóa baseline/schema/lịch sử migration.
Môi trường chung/luôn bật: giữ dịch vụ. Môi trường riêng đang rảnh:
có thể dọn container hợp lệ nhưng GIỮ volume, cấu hình và cách khởi động lại.
Không xóa worktree nếu môi trường giữ lại còn phụ thuộc vào nó.
Giữ tài nguyên đúng chính sách vẫn là hoàn tất housekeeping.

## Dọn tàn tích khi bạn muốn: `/housekeeping`

Phần dọn của `/ship`, không có phần phát hành, cho những việc xong rồi mà chưa
dọn. Bạn gõ `/housekeeping` (Codex: `$housekeeping`) trong thư mục của repo.

1. Agent tìm tàn tích của đúng repo đó: worktree, nhánh cục bộ và trên remote,
   container thử đã dừng. Chưa sửa gì.
2. Chỉ thứ đã gộp hết vào `origin/main` và không phải worktree chính mới được
   tính là dọn được. Thứ chưa gộp được báo lại và giữ nguyên.
3. Agent đưa kế hoạch chia theo phần, rồi hỏi bạn từng phần. Bạn đồng ý phần
   nào thì dọn phần đó.
4. Mục còn vướng (file chưa commit, PR đang mở) được hỏi từng bước một cho tới
   khi dọn được, hoặc bạn bảo giữ. Phiên chat của worktree/nhánh cục bộ được dọn
   thì tự archive luôn, không hỏi riêng (trừ phiên đang chạy sweep và phiên
   đang làm dở).
5. Không bao giờ xoá volume, prune Docker hay đụng vào worktree chính. Mỗi lần
   chạy đều hỏi lại từ đầu.

## Giới hạn

Đây là hướng dẫn cho agent, chưa phải dispatcher hoặc cơ chế cưỡng chế.
Xem [VALIDATION.md](VALIDATION.md). Chưa chạy trên repo/host/Docker của bạn;
20 tình huống agent trong gói là bộ kỳ vọng, chưa phải benchmark đã chạy.
File tự chứa `INSTALL-DEV-SYSTEM.md` và các ZIP dựng cho 4.0 chưa được dựng lại;
cài 4.8.1 từ thư mục này. Script theo dõi theo sự kiện mới chạy thật
một lần (một job Codex, LH-ERP 19/11/2026) ở dạng trước; dạng 5 phút / 40 phút và quy tắc
"builder yếu hơn hỏi lead" chưa chạy thật.
