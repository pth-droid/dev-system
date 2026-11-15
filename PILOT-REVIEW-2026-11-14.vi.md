# Đánh giá Dev System v4.1 sau lượt chạy thật trên LH-ERP (14/11/2026)

Tệp này là kết quả đánh giá, không thuộc gói cài đặt (không có trong `MANIFEST.json`).
Các đề xuất ở mục 4, thẻ lõi ở mục 5 và các điểm rút ra ở mục 6, 7 **đã được áp dụng vào bộ skill thành bản 4.2** ngày 15/11/2026 theo yêu cầu của bạn (xem `CHANGELOG.md`).
Sửa ngày 15/11/2026 (bản 4.3): bản đầu của tệp này và thẻ lõi 4.2 ghi "lead tự chạy lại bằng chứng". Cả hai lỗi lead bắt được đều nhờ xem ảnh cuối và chạy một lệnh kiểm khác, không nhờ chạy lại đúng lệnh cũ; quy tắc đã được sửa thành "lead xem xét bằng chứng, chỉ chạy lại khi đầu vào đã đổi, không có log gốc, hoặc chưa ai chạy".

## 1. Kết luận ngắn

- Dev System v4.1 dùng được cho việc thật và đã bắt được lỗi mà nếu không có nó thì đã lên máy chủ.
- Phần tạo ra giá trị là khoảng 10 quy tắc lõi (mục 3). Phần còn lại của 2.036 dòng hầu như không được mở ra trong lượt này.
- Mười sáu chỗ vướng, mỗi chỗ sửa được bằng một đoạn văn ngắn trong tệp có sẵn, không cần thêm cửa chặn (mục 4).
- QUICK_FIX, bước bấm thử và phát hành kèm dọn dẹp đã chạy xong; nhận xét ở mục 6. Lane LARGE và mục 3a chưa chạy.

## 2. Lượt chạy gồm gì

| Việc | Loại | Kết quả |
|---|---|---|
| J202: Paddle medium, mức suy luận, trần token | STANDARD, 1 builder | Đã lên máy chủ (PR #79) |
| J203: script triển khai bỏ sót bước, dòng tên rỗng | Sửa lỗi nhỏ có hành vi | Đã lên máy chủ (PR #81) |
| J201: tự đề xuất mã và đơn vị khi soát ảnh hoá đơn | STANDARD, 4 task, 1 builder | Đã lên máy chủ (PR #83), kèm QF1 |

J201 và J202 chạy song song trên hai worktree, không đụng tệp của nhau.

## 3. Quy tắc nào đã tạo ra giá trị

| Quy tắc | Nó bắt được gì trong lượt này |
|---|---|
| Kiểm máy chủ đang chạy bản nào trước khi làm | Máy chủ OCR còn ở bản 09/11, chưa có model dự phòng; workspace Codex hết credit nên đọc online đang lỗi |
| Đo trước khi quyết | Công thức so chữ của dịch vụ đúng 55 %, công thức cũ đúng 81 %; luật lấy đơn vị từ tên sai 3 trên 6; sàn 0,70 giả định đổi thành 0,30 đo được |
| Lead xem xét bằng chứng (ảnh cuối, lệnh kiểm độc lập), không tin câu "đạt" | Test giao diện đạt 60/60 nhưng ảnh chụp cuối cho thấy đơn vị bị đổi từ Hộp sang ml; script triển khai báo thành công nhưng thiếu model medium |
| Thẻ quyết định cho chủ doanh nghiệp | 8 quyết định của J201 được ghi lại kèm phương án đã bỏ |
| Trạng thái bằng chứng trung thực | AC-04 ghi rõ là chưa làm được thay vì báo xong |
| Commit cục bộ, ứng viên là mã commit | Soát phần sửa chỉ cần xem chênh lệch giữa hai commit |
| Builder cũ sửa lỗi của chính nó | Hai lần sửa sau soát đều được chấp nhận ở lần soát kế tiếp (lần hai kèm một sửa nhỏ của lead) |
| Sổ tài nguyên | Biết chính xác stack thử nào là của việc này để không đụng stack khác |

## 4. Chỗ vướng và đề xuất sửa

Mỗi mục ghi rõ nó thêm việc hay bớt việc. Không mục nào là cửa chặn máy móc.

### 4.1 Thẻ quyết định nói sai về hành vi hiện tại (thêm 1 dòng)
- **Đã xảy ra:** tôi viết "món đỏ vẫn tạo được phiếu nháp như hôm nay" mà chưa đọc mã; thực tế đang bị chặn. Bạn đã chọn dựa trên câu sai đó.
- **Sửa ở:** `dev-guardrails/references/discovery.md`, mục "Use one decision card per consequential question".
- **Nội dung:** mỗi câu trong thẻ nói về hành vi hiện tại phải kèm nguồn (`tệp:dòng` hoặc lệnh đã chạy). Chưa kiểm thì ghi "chưa kiểm".

### 4.2 Quyết định không thực hiện được vì lớp sau từ chối (thêm 1 bước)
- **Đã xảy ra:** "đỏ nhưng không chặn" được chốt, đến task thứ ba mới biết lớp kế toán từ chối phiếu có dòng thiếu mã.
- **Sửa ở:** `dev-guardrails/references/planning-handoff.md`, mục "Divide by demonstrable outcome".
- **Nội dung:** quyết định nào bỏ hoặc nới một điều kiện chặn thì trước khi ghi vào hợp đồng hành vi phải lần theo dữ liệu thêm một bước về phía sau và ghi lớp nào nhận nó.

### 4.3 Câu hỏi chờ chủ doanh nghiệp bị trôi (bớt chờ)
- **Đã xảy ra:** câu hỏi về món đỏ được hỏi lại nhiều lần qua nhiều lượt trao đổi mà chưa có trả lời, vì trong lúc đó có nhiều yêu cầu khác chen vào.
- **Sửa ở:** `workflow/daily-workflow.md`, mục 14 "Owner status report".
- **Nội dung:** mỗi báo cáo mở đầu bằng danh sách quyết định đang chờ, mỗi dòng có mã, ngày hỏi, phương án mặc định. Với quyết định đảo lại được, lead đi tiếp theo phương án thận trọng hơn và ghi rõ "đang đi theo mặc định, đổi được".

### 4.4 Yêu cầu thêm giữa chừng (bớt tranh luận)
- **Đã xảy ra:** nhiều yêu cầu thêm trong lúc J201 đang chạy (đơn vị theo hoá đơn, đơn vị trong tên, đổi Paddle, mức suy luận, trần token, bí danh hiệu lực ngay). Tách J202 ra riêng là đúng; gộp đơn vị vào J201 cũng đúng. Cả hai lần tôi phải tự nghĩ ra tiêu chí.
- **Sửa ở:** `workflow/dev-router.md`, mục 6 "Reclassify when evidence changes".
- **Nội dung:** yêu cầu mới cùng màn hình và cùng lần triển khai thì thêm AC vào hồ sơ đang mở. Khác thành phần triển khai hoặc tự đứng được một mình thì mở việc mới và chạy song song.

### 4.5 Môi trường thử lộ ra muộn (thêm 1 dòng ở kế hoạch)
- **Đã xảy ra:** đến task 2 của J201 mới biết cần một stack riêng; dựng stack mất thêm một vòng và để lại vài lỗi môi trường phải tách khỏi lỗi thật.
- **Sửa ở:** `workflow/daily-workflow.md`, mục 3a "Provision the change workspace before development".
- **Nội dung:** bảng task có thêm cột "bằng chứng chạy ở đâu". Môi trường nào chưa khởi động được thì dựng trước khi giao task đầu tiên.

### 4.6 Tệp dùng chung va nhau khi chạy song song (bớt xung đột)
- **Đã xảy ra:** `docs/PROGRESS.md` xung đột khi gộp main vào J201 vì ba việc cùng thêm dòng ở một chỗ.
- **Sửa ở:** `workflow/daily-workflow.md`, mục 1, đoạn về chạy song song.
- **Nội dung:** giữ số quyết định ngay khi mở việc. Tệp nhật ký dùng chung chỉ do lead ghi, một lần, ngay trước khi tạo PR và sau khi đã gộp main.

### 4.7 Sửa một dòng mà phải gọi lại builder (bớt chi phí)
- **Đã xảy ra:** ở lượt sửa hai lỗi đơn vị, ngữ cảnh của builder đã lên khoảng 520.000 token, nên mỗi bước của lượt sửa phải đọc lại chừng ấy. (Bản đầu ghi "lượt sửa tốn 523.753 token"; con số đó là độ dài ngữ cảnh, không phải lượng tiêu. Đo lại ngày 15/11: cả builder J201, gồm bốn task và các lượt sửa, tốn 158 lượt gọi và khoảng 11,94 USD giá niêm yết.) Lỗi thứ ba chỉ là một biểu thức, tôi tự sửa và chạy lại test trong vài phút.
- **Sửa ở:** `workflow/daily-workflow.md`, mục 9 "Feedback -> fix -> delta recheck".
- **Nội dung:** lead được tự sửa khi thay đổi không quá khoảng 5 dòng, không có quyết định hành vi mới, và lead chạy lại bài test liên quan. Ghi rõ trong báo cáo là lead sửa. Lớn hơn thì trả về builder như hiện nay.
- **Lưu ý:** lần tự sửa đó tôi làm hỏng cú pháp ở lần gõ đầu; `node --check` bắt được. Quy tắc phải giữ điều kiện "chạy lại kiểm tra".

### 4.8 Test giao diện đạt nhưng màn hình sai (thêm 1 thói quen)
- **Đã xảy ra:** bài test kiểm đơn vị sau bước chọn mã đầu tiên rồi không kiểm lại; lỗi nằm ở bước sau. Bài test cũng mở cửa sổ soát bằng lệnh nội bộ, bỏ qua đường bấm từ màn hình chính.
- **Sửa ở:** `dev-guardrails/references/verification.md`, mục "Choose evidence with the least duplicate work".
- **Nội dung:** với thay đổi nhìn thấy được, lead xem ảnh chụp trạng thái cuối. Giá trị không được phép đổi thì kiểm lại sau mỗi bước, không kiểm một lần. Trước khi mời chủ doanh nghiệp bấm thử, lead tự đi đúng đường bấm đó một lần.

### 4.9 "Script báo thành công" chưa phải là đã triển khai (thêm 1 dòng)
- **Đã xảy ra:** `Update-LhOcr.ps1` in "deployed" trong khi bỏ sót mọi bước sau lần kiểm sức khoẻ đầu.
- **Sửa ở:** `release-housekeeping/references/deploy-and-migrate.md`.
- **Nội dung:** sau triển khai, kiểm trạng thái thật của thứ vừa đổi (bản đang chạy, tệp có mặt, một lần chạy thật) bằng lệnh độc lập với script. Đường quay lui chưa từng chạy thì ghi là chưa kiểm.

### 4.10 Mẫu biểu trùng với runbook của repo (bớt giấy tờ)
- **Đã xảy ra:** LH-ERP đã có `AGENTS.md`, runbook triển khai và sổ quyết định. `project-setup.md` và mẫu hồ sơ phát hành không thêm thông tin gì.
- **Sửa ở:** `workflow/project-setup.md` phần đầu, và `dev-guardrails/references/worktree.md` mục "Before any writes".
- **Nội dung:** repo đã có tài liệu tương đương thì chỉ ghi đường dẫn tới nó, không điền mẫu. Vị trí worktree theo quy ước của repo.

### 4.11 Con số trong báo cáo bị trôi (thêm 1 dòng)
- **Đã xảy ra:** tôi ghi "67 test" qua nhiều lượt, thực tế là 57. Sai lệch sinh ra khi tóm tắt lại từ trí nhớ.
- **Sửa ở:** `dev-guardrails/SKILL.md`, mục 5 "Report an honest result".
- **Nội dung:** số liệu trong báo cáo chép từ dòng kết quả của lệnh vừa chạy, không chép từ báo cáo trước.

### 4.12 Builder của việc nhỏ chạy model đắt nhất (bớt chi phí)
- **Đã xảy ra:** tôi gọi builder cho QF1 mà không chỉ định model, nên nó thừa hưởng Fable. Bạn phải nhắc. Chạy lại bằng Sonnet: một lượt, 131.701 token, khoảng 5 phút, lead không phải trả lại lần nào. Lượt sửa T3 trước đó tốn 523.753 token.
- **Sửa ở:** `workflow/dev-router.md`, bảng lane ở mục 2 và mục 3b bước 3.
- **Nội dung:** mỗi lane ghi mức model mặc định cho builder: QUICK_FIX và task STANDARD đã chốt thiết kế dùng model rẻ hơn; model của lead chỉ dùng cho việc nặng thiết kế hoặc rủi ro cao. Lead chỉ định model ở mỗi lần gọi.

### 4.13 Bài kiểm bắt buộc của repo lộ ra lúc phát hành (thêm 1 dòng)
- **Đã xảy ra:** runbook LH-ERP bắt buộc ba bài quét vỏ trước mọi lần triển khai có sửa `/ketoan`. Tôi để chúng ở mức "builder báo, lead chưa chạy" cho tới lúc phát hành; lần đầu tự chạy thì cả ba lỗi vì thiếu tên người dùng thử.
- **Sửa ở:** `dev-guardrails/references/verification.md` và mẫu `change-record.md`.
- **Nội dung:** bài kiểm mà runbook của repo bắt buộc trước triển khai phải có một lần chạy được ghi lại trên commit ứng viên trước READY_FOR_PR (builder hoặc runner rẻ chạy, lead đọc kết quả). Hồ sơ ghi nguyên lệnh chạy (kèm biến môi trường) của mỗi bằng chứng, để người khác chạy lại được.

### 4.14 Phản hồi sau khi chủ doanh nghiệp bấm thử chưa có đường đi (bớt tranh luận)
- **Đã xảy ra:** bấm thử sinh ra hai loại phản hồi: sửa trình bày nhỏ (QF1, làm ngay trước phát hành) và đổi thiết kế (đưa thao tác vào trong bảng, là một việc STANDARD mới). Workflow chỉ có hai kết quả "OK" và "cần sửa".
- **Sửa ở:** `dev-guardrails/references/verification.md`, mục owner check.
- **Nội dung:** mỗi phản hồi sau bấm thử được phân lane lại như một yêu cầu mới. QUICK_FIX cùng màn hình thì làm trên nhánh đang mở trước khi phát hành; lớn hơn thì phát hành bản hiện tại (nếu nó không tệ hơn bản đang chạy) và mở việc mới.

### 4.15 Bản giao việc đặt sai tiền đề nhỏ (thêm 1 dòng)
- **Đã xảy ra:** tôi viết "chọn tài khoản xong thì ô hết đỏ như F4 hiện nay"; thực tế F4 cũng không làm ô hết đỏ cho tới khi Lưu. Builder tự thêm một quy tắc hiển thị và báo lại. Kết quả đúng, nhưng quy tắc "thiết kế không đứng được thì DỪNG" không nói rõ trường hợp này.
- **Sửa ở:** `dev-guardrails/references/planning-handoff.md`, phần quy tắc cho builder.
- **Nội dung:** sai lệch không đổi hành vi nghiệp vụ, dữ liệu hay điều kiện chặn thì builder xử lý theo ý định của bản giao việc và báo rõ; sai lệch chạm vào các thứ đó thì dừng.

### 4.16 Dọn dẹp khi đã có việc nối tiếp (bớt dựng lại)
- **Đã xảy ra:** bạn cho dọn ngay sau phát hành, nhưng cũng vừa yêu cầu một việc mới trên cùng màn hình. Xoá stack thử `j201` rồi dựng lại sẽ tốn thêm một vòng.
- **Sửa ở:** `release-housekeeping/references/cleanup.md`.
- **Nội dung:** trước khi dọn môi trường thử, kiểm có việc nối tiếp đã được yêu cầu trên cùng khu vực không. Có thì giữ môi trường, ghi vào sổ tài nguyên là chuyển cho việc mới, và vẫn xoá nhánh đã gộp.

## 5. Độ nặng

- Bộ skill dài 2.036 dòng. Trong lượt này tôi chủ yếu mở lại `verification.md`, `daily-workflow.md` mục 9 và 11, và mẫu `change-record.md`. Các tệp còn lại hầu như không được mở sau lần đọc đầu.
- Đề xuất: thêm một trang "thẻ lõi" khoảng 40 dòng ở đầu `dev-guardrails/SKILL.md`, gồm đúng các quy tắc ở mục 3 và các bổ sung ở mục 4. Các tệp tham chiếu giữ nguyên, chỉ mở khi cần.
- Chi phí lớn nhất không nằm ở giấy tờ mà ở số vòng builder: J201 cần 6 vòng (T1, sửa F-01, T1b, T2, T3, sửa T3). Mục 4.2 và 4.5 nhằm vào đúng hai vòng lẽ ra tránh được.

## 6. Ba phần chạy sau cùng (bổ sung 14/11, sau khi J201 phát hành)

### QUICK_FIX mục 3b (QF1)
- **Chạy tốt.** Từ lúc bạn duyệt tới lúc có commit đã soát: một bản giao việc, một builder, một lượt, không có vòng sửa.
- **Thứ làm nó nhanh** là sáu quyết định trình bày chốt sẵn trong bản giao việc, không phải bản thân lane. Lead đọc mã trước khi viết bản giao việc đã sửa được hai điều tôi nói sai với bạn ở lượt trước (bảng chi phí vốn đã tách riêng; ô Kho có được dùng).
- **Ranh giới 3a / 3b rõ và dùng được:** năm điểm sửa chia ra hai điểm chỉ đổi chữ và ba điểm có điều kiện hiển thị; gộp làm một việc 3b là hợp lý vì cùng tệp.
- **Thiếu:** mức model cho builder (mục 4.12).
- **Mục 3a** vẫn chưa chạy riêng lần nào.

### Bước chủ doanh nghiệp xem tận mắt
- **Đây là bước tạo ra nhiều giá trị nhất của lượt chạy.** Test tự động đạt 80/80 nhưng bạn nhìn màn hình và thấy ngay phần dưới khó hiểu; không bài test nào bắt được điều đó.
- **Gói bấm thử thiếu hai thứ:** chỗ lấy mật khẩu và tên đăng nhập (bạn phải hỏi lại), và lời giải thích từng vùng trên màn hình. Nên thêm vào mẫu owner check: địa chỉ, tên đăng nhập, nơi lấy mật khẩu, và một ảnh có chú thích.
- **Thiếu:** đường đi cho phản hồi sau bấm thử (mục 4.14).

### Phát hành và dọn dẹp (`release-housekeeping`)
- **Chạy được trọn chuỗi:** PR #83, gộp `040aaae`, triển khai 3 phút 48, kiểm bản thật trên máy chủ, bấm thử trên máy chủ bằng người dùng thử rồi xoá, PR tài liệu #84, xoá sáu nhánh và một worktree.
- **Skill giúp ở hai điểm:** bắt đọc runbook của repo trước (nhờ đó mới chạy ba bài quét vỏ), và tách "đã gộp", "đã triển khai", "đã kiểm" thành ba việc riêng.
- **Skill không giúp ở:** lỗi 502 của GitHub khi gộp. Tôi đã nối lệnh "gộp" với "chuyển worktree sang main" trong một lần chạy, nên khi gộp lỗi thì worktree bị chuyển về main cũ. Nên thêm một dòng: kiểm kết quả của bước hướng ra ngoài trước khi chạy bước phụ thuộc vào nó.
- **Lệnh ngắn `/ship`** được tạo theo yêu cầu của bạn; chưa thử ở phiên mới.
- **Lane LARGE:** không dùng tới.

## 7. Lượt J204 (bổ sung 15/11): thử lại workflow với các đề xuất ở mục 4

J204 là việc STANDARD sinh ra từ lần bạn bấm thử J201. Tôi chạy nó theo workflow hiện tại cộng với sáu đề xuất ở mục 4, để xem các đề xuất có tác dụng thật không.

| Đề xuất đã thử | Áp dụng thế nào | Kết quả |
|---|---|---|
| 4.1 Đọc mã trước khi nói về hành vi hiện tại | Lead đọc trình soạn phiếu trước khi viết kế hoạch | Tìm ra hộp thả xuống dùng chung có sẵn; không phải dựng mới |
| 4.3 Quyết định chờ có phương án mặc định | Câu "giữ hay bỏ dòng tóm tắt" ghi là "mặc định, đổi được" | Việc không dừng chờ; bạn duyệt luôn khi bấm thử |
| 4.5 Ghi bằng chứng chạy ở đâu | Bảng task có cột môi trường; dùng lại stack `j201` | Không mất vòng dựng môi trường. Vẫn lộ một thiếu sót của site thử (trường chi nhánh của Kho) |
| 4.12 Model theo lane | Builder Sonnet cho cả ba task | Khoảng 426 nghìn token cho ba task, lead không phải trả lại lần nào |
| 4.15 Quy tắc sai lệch cho builder | Bản giao việc ghi rõ khi nào tự xử lý, khi nào dừng | Builder tự đổi một chi tiết giao diện đúng hướng, và dừng báo khi gặp lỗi ở phần lập chứng từ |
| 4.16 Giữ môi trường khi có việc nối tiếp | Stack `j201` và worktree được giữ sau J201 | J204 bắt đầu ngay, không dựng lại |

Ba điều mới rút ra:

- **Quy tắc "mốc không xanh thì dừng" đáng giá hơn chi phí của nó.** Builder dừng một vòng vì bài test lập nháp có sẵn một lỗi. Nhờ vậy lỗi của môi trường không bị lẫn với lỗi do thay đổi mới.
- **Builder tìm ra một lỗi cũ liên quan tới chứng từ** (phiếu chi phí nháp bỏ qua dòng đã sửa) nhờ lần theo dữ liệu thêm một bước. Workflow chưa nói rõ lỗi cũ lộ ra giữa chừng thì gộp vào việc đang làm hay tách riêng. Đề xuất: gộp khi việc đang làm khiến lỗi đó dễ gặp hơn, và ghi thành một AC riêng để chủ doanh nghiệp duyệt lúc bấm thử.
- **Gói bấm thử lần hai đủ dùng:** có địa chỉ, tên đăng nhập, bảy bước và hai điều cần duyệt; bạn trả lời bằng hai chữ "Ship đi" và lệnh `/ship` tự chạy.

Chỗ còn vướng: bản giao việc yêu cầu builder ghi tệp báo cáo nhưng môi trường chạy không cho phép; và tôi điền sai số cột của hai bảng sổ ở lần đầu. Cả hai đều là chi tiết của repo, không phải của workflow.
