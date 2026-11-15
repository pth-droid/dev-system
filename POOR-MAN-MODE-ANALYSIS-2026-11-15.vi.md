# Phân tích "poor man mode": làm việc tiếp khi hạn mức sắp hết (15/11/2026)

Tệp này ghi lại toàn bộ suy luận, số đo và các kết luận đã bị bác trong buổi trao đổi ngày 15/11/2026.
Nó không thuộc gói cài đặt (không có trong `MANIFEST.json`).

## 0. Dùng tệp này khi nào và thế nào

Mở lại khi có một trong các việc sau: model mới ra, bảng giá đổi, chính sách hạn mức của gói đổi, hoặc host đổi cách tính cache.

1. Cập nhật bảng giá ở mục 2.
2. Chạy lại các script ở mục 9 trên một lượt làm việc thật gần nhất.
3. Đối chiếu từng dòng ở mục 8 ("điều gì làm kết luận đổi").
4. Sửa mục 7 (đã quyết gì) nếu kết luận đổi, rồi mới sửa bộ skill.

## 1. Câu hỏi và kết luận ngắn

**Câu hỏi ban đầu:** có nên dựng một tier 4 thay cho builder và tester tier 3, để chủ dự án bật "poor man mode" vào những ngày hạn mức sắp hết?

**Kết luận tại ngày 15/11/2026:**

- Poor man mode không đáng dựng thành một chế độ riêng. Builder chỉ chiếm 29% chi phí của lượt thí điểm; lead chiếm 71%.
- Phần tiết kiệm lớn đến từ các cơ chế không đánh đổi chất lượng. Chúng thuộc về chế độ thường: lead chạy Opus (đúng như bộ skill quy định), giữ ngữ cảnh lead ngắn, vào ra gọn, mỗi task một builder mới.
- Chỉ có hai công tắc thật sự đánh đổi chất lượng: hạ model của người viết mã, và hạ model của lead. Cả hai chưa được thử.
- Thứ đã viết vào bộ skill: QUICK_FIX đủ điều kiện thì chạy ở một phiên mới với model rẻ rồi báo về (dev-router.md mục 3c); giữ ấm cache cho phiên lead (daily-workflow.md mục 7a); chọn model theo độ dài ngữ cảnh của vai.

## 2. Giá đã dùng (USD mỗi triệu token)

| Model | Đầu vào | Đầu ra | Đọc cache | Ghi cache 1 giờ | Ngưỡng tăng giá | Nguồn |
| --- | --- | --- | --- | --- | --- | --- |
| Fable 5.2 | 8 | 40 | 0,20 | 16 | không | Tài liệu tham chiếu đi kèm Claude Code |
| Opus 5.5 | 4 | 20 | 0,20 | 8 (suy ra, gấp đôi đầu vào) | không | Như trên |
| Sonnet 5.5 | 2 | 10 | 0,10 | 4 (suy ra) | không | Như trên |
| Haiku 5.5 | 0,10 rồi 0,50 | 0,50 rồi 2,50 | chưa có | chưa có | 100K | Như trên, và bảng chủ dự án dán |
| Sol 6.1 | 2 rồi 4 | 10 rồi 15 | chưa có | chưa có | 272K | Bảng chủ dự án dán, tôi chưa kiểm |
| Terra 6.1 | 1 rồi 2 | 5 rồi 7,5 | chưa có | chưa có | 272K | Bảng chủ dự án dán, tôi chưa kiểm |

Mọi con số USD trong tệp này là giá API niêm yết, dùng để so sánh tương đối. Gói Team tính phần trăm hạn mức theo cách riêng mà tôi chưa đo được (mục 10).

## 3. Số đo

Nguồn: nhật ký của phiên lead và 11 nhật ký agent con, lượt thí điểm Dev System trên LH-ERP từ 15:20 ngày 14/11 tới sáng 15/11/2026 (J201, QF1, J202, J204, hai lần phát hành, đánh giá).

### 3.1 Phiên lead (Fable 5.2, 348 lượt gọi)

| Phần | Token | USD | Tỉ lệ |
| --- | --- | --- | --- |
| Đọc lại ngữ cảnh từ cache | 127.634.746 | 25,53 | 35,7% |
| Đầu ra, gồm cả suy nghĩ | 591.856 | 23,67 | 33,1% |
| Ghi nội dung mới vào cache | 1.398.095 | 22,37 | 31,3% |
| Tổng | | 71,58 | |

- Ngữ cảnh mỗi lượt gọi: trung vị 291.845, phân vị 90 là 729.759, cao nhất 832.044. Có 107 trên 348 lượt gọi chạy với ngữ cảnh trên 500.000 token.
- Đầu ra mỗi lượt gọi: trung vị 1.295, phân vị 90 là 3.863.
- Khởi động nguội: bốn lần ghi trên 50.000 token, tổng 252.371 token, 4,04 USD (6% tổng). Hai lần sau quãng nghỉ dài (205 và 524 phút) mỗi lần chỉ ghi khoảng 61.000 token vì trùng lúc ngữ cảnh vừa được nén.
- Phần cố định của một phiên: khoảng 58.000 token (công cụ hệ thống 20.088, công cụ MCP 13.738, chỉ dẫn hệ thống 11.897, skill 9.966, bộ nhớ 2.200).

### 3.2 Các agent con

| Agent | Model | Lượt gọi | USD |
| --- | --- | --- | --- |
| Builder J201 (bốn task và các lượt sửa) | Sonnet | 158 | 11,94 |
| Builder J204 | Sonnet | 159 | 9,55 |
| Builder J202 | Sonnet | 74 | 4,15 |
| Builder QF1 chạy nhầm Fable rồi dừng | Fable | 8 | 2,83 |
| Builder QF1 chạy lại | Sonnet | 26 | 0,99 |
| Tra cứu | Sonnet | 7 | 0,36 |
| Năm lượt Haiku đọc hoá đơn | Haiku | 15 | chưa quy ra tiền |
| Tổng | | 447 | 29,83 |

- Tổng của 11 agent: đầu ra 523.356, đọc cache 110.459.187, ghi cache 3.260.412. Phần ghi tính theo giá một giờ nên là cận trên.
- Builder tốn 81% vào đọc và ghi ngữ cảnh, 18 đến 19% vào đầu ra.
- Ngữ cảnh builder: lượt đầu khoảng 58.000 token; trung vị J201 là 331.574, J204 là 327.677, J202 là 152.427; cao nhất 521.041 (J201).
- Tỉ lệ lượt gọi trên 100K: J201 97%, J204 97%, J202 86%. Trên 272K: J201 61%, J204 58%, J202 0%.
- Các lượt gọi chạy bài kiểm chiếm 27,6% chi phí builder J201, 44,1% của J204, 28,1% của J202.
- Số dòng trong thay đổi đã gộp: J201 kèm QF1 thêm 983 dòng test, 320 dòng mã, 118 dòng tài liệu. J204 thêm 347 dòng test, 143 dòng mã.
- Con số `total_tokens` mà agent con báo về (ví dụ 523.753) là độ dài ngữ cảnh ở lượt gọi cuối, không phải lượng đã tiêu.

### 3.3 Cả lượt thí điểm

Khoảng 101 USD: lead 71%, agent con 29%. Trên Fable khoảng 74 USD.

### 3.4 Hạn mức gói Team (đọc ngày 15/11/2026)

- Ba hạn mức: 5 giờ, tuần cho mọi model, tuần riêng cho Fable. Chưa bật dùng thêm ngoài gói.
- Từ 09:07 tới khoảng 10:40, phiên lead tốn 8,26 USD; hạn mức 5 giờ đi từ 3% lên 9%, tuần mọi model từ 35% lên 36%, tuần Fable từ 27% lên 29%.
- Ước lượng thô: khoảng 1 USD giá niêm yết cho mỗi điểm phần trăm của hạn mức 5 giờ. Tôi giả định không có phiên nào khác chạy cùng lúc, và con số chỉ chính xác tới 1%.

### 3.5 Phát lại 391 lượt gọi của ba builder chính theo giá có ngưỡng

Giả định: mọi model có tỉ lệ cache như Sonnet (đọc bằng 5% giá đầu vào, ghi gấp đôi), và ngưỡng tính trên toàn bộ đầu vào kể cả phần đọc từ cache.

| Model | Như đã chạy | Nếu mọi lượt gọi dưới ngưỡng |
| --- | --- | --- |
| Sonnet 5.5 | 25,64 | 25,64 |
| Haiku 5.5 | 6,13 | 1,28 |
| Terra 6.1 | 18,71 | 12,82 |
| Sol 6.1 | 37,42 | 25,64 |

## 4. Các suy luận theo thứ tự, kể cả chỗ đã sai

Ghi lại để lần sau không đi lại đường cũ.

1. **"Lead tốn nhất vì ngữ cảnh dài."** Tôi nói vậy trước khi đo. Sau đó tôi rút lại vì giá đọc cache chỉ bằng 1/40 giá đầu vào trên Fable. Số đo cho thấy cả hai đều đúng một nửa: từng bước thì rẻ, nhưng 348 bước với ngữ cảnh trung bình 367.000 token vẫn là khoản lớn nhất (35,7%).
2. **"Lead chạy lại bằng chứng là lãng phí."** Đúng về logic (chạy lại cùng lệnh trên cùng commit không phát hiện thêm gì), nhưng về tiền chỉ khoảng 0,1 đến 0,2 USD mỗi lần. Hai lỗi lead bắt được trong thí điểm đều nhờ nhìn ảnh cuối và chạy một lệnh kiểm khác. Đã sửa thẻ lõi ở bản 4.3.
3. **"Phát hành nên chạy ở phiên mới với model rẻ."** Ước tính: lead Fable còn ấm khoảng 3,7 USD, agent con Sonnet khoảng 1,4 USD, phiên Sonnet mới khoảng 1,2 USD cho 40 bước. Chênh lệch đến từ giá model, không phải độ dài ngữ cảnh. Lý do chọn phiên mới chủ yếu không phải chi phí: tác giả không tự phát hành, phiên mới xoá được worktree, và nó kiểm luôn hồ sơ có đủ không.
4. **"Khởi động nguội là khoản lớn, nên cần giữ ấm cache."** Theo giá, ghi cache một giờ đắt gấp 80 lần đọc cache trên Fable và 40 lần trên Opus, nên giữ ấm có lợi. Nhưng đo thực tế thì khởi động nguội chỉ chiếm 6% của phiên này. Giữ ấm vẫn được viết vào skill (mục 7a) vì thói quen nhiều phiên ngắn trong ngày của chủ dự án, với hiểu biết rằng lợi ích nhỏ.
5. **"`/compact` trước khi nghỉ là cách không cần cơ chế."** Nói quá. Nén chỉ thu nhỏ điểm xuất phát, phần còn lại vẫn phải ghi lại ở lượt kế tiếp, ngữ cảnh lại dài ra khi soát, và nén sau khi đã nguội thì không tiết kiệm gì.
6. **"Tier 4 cho builder sẽ tiết kiệm nhiều."** Builder chỉ là 29% tổng. Hạ effort của builder gần như vô ích vì đầu ra chỉ là 18% chi phí builder. Hạ bậc model thì có tác dụng: Haiku rẻ hơn Sonnet 4 lần trên ngưỡng 100K.
7. **"Ngưỡng 100K của Haiku cho mức rẻ 20 lần."** Gần như không đạt được cho việc build, vì một agent con đã ở 58.000 token lúc khởi động.
8. **"Sol 6.1 tương đương Sonnet."** Giá niêm yết bằng nhau, nhưng với builder ngữ cảnh dài thì Sol đắt hơn 46% vì ngưỡng 272K.
9. **"Poor man mode là một chế độ ba mức."** Sau khi chuyển các cơ chế không đánh đổi sang chế độ thường, nó chỉ còn hai công tắc hạ model. Sau đó chủ dự án chỉ ra rằng phần còn lại trùng với QUICK_FIX, nên nó thành một quy tắc về nơi chạy của QUICK_FIX.
10. **"Việc đơn giản là một làn mới."** Sai. Về phạm vi nó chính là QUICK_FIX; chỉ có nơi chạy và điều kiện "đã có thứ để kiểm" là mới.

## 5. Các cơ chế và ước tính

Ước tính là phép tính trên khối lượng đã đo với mức giảm giả định. Chưa có cơ chế nào được đo bằng một lượt chạy thật.

### 5.1 Trên tổng 101 USD của lượt thí điểm (lead Fable)

| Cơ chế | Ước tính | Cái giá |
| --- | --- | --- |
| Lead dùng Opus thay Fable | giảm 23% | Phán đoán yếu đi một bậc |
| Giữ ngữ cảnh lead dưới 150.000 token | giảm 15% | Mỗi thay đổi một phiên, hồ sơ phải đủ |
| Builder rẻ trước, lên bậc khi bài kiểm lỗi | giảm tới 13% | Cần tín hiệu lỗi đáng tin |
| Đầu ra của lead gọn hơn | giảm 9% | Ít giải thích |
| Đầu vào của lead gọn hơn (log ra tệp) | giảm 6% | Không đáng kể |
| Mỗi task một builder mới | giảm khoảng 6% | Builder mới đọc lại tệp |
| Giữ ấm cache | giảm 2 đến 4% | Đã làm |

### 5.2 Khi lead chạy Opus

| Kịch bản | Lead | Builder | Tổng | Phần của builder |
| --- | --- | --- | --- | --- |
| Đã chạy: lead Fable | 71,6 | 27,0 | 98,6 | 27% |
| Lead Opus | 48,6 | 27,0 | 75,6 | 36% |
| Lead Opus, ngữ cảnh ngắn, vào ra gọn | khoảng 25,5 | 27,0 | khoảng 52,5 | 51% |

Trên nền 52,5 USD: người viết mã xuống tier 4 (test giữ ở tier 3) giảm khoảng 8,5 USD (16%); lead xuống Sonnet giảm khoảng 12,7 USD (24%); cả hai khoảng 40%.

### 5.3 Phía builder (trên 27 USD)

| Cơ chế | Ước tính |
| --- | --- |
| Giảm effort | giảm 1,5 đến 2 USD |
| Mỗi task một builder mới | giảm khoảng 6 USD |
| Hạ từ Sonnet xuống Haiku (giả định thêm 50% lượt gọi) | giảm khoảng 17 USD |

## 6. Kiến trúc đã bàn nhưng chưa dựng

### 6.1 Tách người viết test khỏi người viết mã

Chỉ dùng khi người viết mã là model dưới bậc Sonnet, và chỉ cho việc có hành vi mới.

1. Lead cùng chủ dự án viết bảng tình huống bằng lời thường: đầu vào, kết quả mong đợi, giá trị không được đổi, trường hợp phải từ chối.
2. Một lượt model mạnh nhất còn dùng được, ngữ cảnh mới, soát bảng. Nếu không còn model mạnh, chủ dự án soát.
3. Người viết test (tier 3) viết test từ bảng, chạy cho thấy lỗi trên mã hiện tại, commit riêng.
4. Lead đọc các dòng khẳng định, ghi mã commit của test.
5. Người viết mã (tier 4), mỗi task một builder mới. Không được đổi giá trị mong đợi hay câu khẳng định; thấy test sai thì dừng và báo. Với test giao diện, được sửa phần tìm nút và thao tác chuột.
6. Thử hai lần không đạt thì giao cho builder bậc Sonnet.
7. Runner chạy toàn bộ bài kiểm trên commit cuối, log ra tệp.
8. Lead kiểm tệp test không đổi kể từ lúc khoá, đọc diff mã, nhìn trạng thái cuối.

Lý do đặt tier 3 ở khâu test: mã sai thì có test bắt, test sai thì không có gì bắt. Hai agent tier 4 chỉ chấp nhận được khi bảng tình huống cụ thể tới từng con số, test là loại tính toán thuần, và việc không chạm sổ sách, phân quyền hay migration.

Kiến trúc này giữ độ tin cậy khi model yếu đi; nó không phải cơ chế tiết kiệm chính.

### 6.2 Các việc khác chưa làm

- `/ship` giao phần thực thi cho agent con Sonnet, lead chỉ giao việc, đọc báo cáo và kiểm độc lập.
- Mỗi task một builder mới, và giới hạn việc dùng lại builder khi ngữ cảnh sắp qua ngưỡng giá của model.
- Chế độ in gọn cho script test của LH-ERP (chỉ in dòng lỗi và dòng tổng).
- Ngoại lệ trong `AGENTS.md` toàn cục mục 1, nơi đang ghi "không mở phiên Claude riêng trừ khi được yêu cầu".
- Cắt bớt công cụ và skill không dùng để giảm 58.000 token khởi động.

## 7. Đã quyết và đã viết vào bộ skill

| Bản | Nội dung | Chỗ |
| --- | --- | --- |
| 4.3 | Giữ ấm cache cho phiên lead, kèm kiểm tiến độ; dừng theo thứ đang chờ; bật tắt bằng lời | daily-workflow.md 7a, lệnh `/warm`, `AGENTS.md` mục 7 |
| 4.3 | Lead xem xét bằng chứng, chỉ chạy lại khi đầu vào đổi | Thẻ lõi dòng 8, verification.md |
| 4.4 | QUICK_FIX đủ năm điều kiện thì chạy ở phiên mới với model rẻ, báo về trong 400 ký tự đầu | dev-router.md 3c |
| 4.4 | Thêm Terra 6.1 xHigh vào tier 3 | daily-workflow.md mục 2 |
| 4.4 | Chọn model theo độ dài ngữ cảnh của vai; ghi ngưỡng tăng giá | daily-workflow.md mục 2, project-setup.md |

Năm điều kiện của mục 3c: đã có thứ để kiểm; thiết kế nói được trong một câu; nằm gọn trong vài tệp của một module; không ghi dữ liệu và không chạm sổ sách, phân quyền, tiền, migration; hoàn lại một commit là quay lui được.

## 8. Điều gì làm kết luận đổi

| Nếu | Thì xét lại |
| --- | --- |
| Giá đọc cache của model lead không còn nhỏ hơn nhiều so với giá ghi | Giữ ấm cache; lợi ích của phiên dài |
| Giá đọc cache của Opus thấp hơn của Fable | Mức tiết kiệm khi lead chạy Opus (hiện bằng nhau nên chỉ giảm 32%) |
| Có model rẻ hơn Sonnet mà không có ngưỡng tăng giá | Model cho builder ngữ cảnh dài và cho người viết test |
| Ngưỡng của Haiku nâng lên trên 100K, hoặc phần khởi động của agent con giảm rõ dưới 58.000 token | Mức rẻ 20 lần của Haiku trở nên đạt được |
| Một model tier 4 làm xong một việc STANDARD trong thí điểm với số lượt lên bậc thấp | Dựng kiến trúc ở mục 6.1 |
| Sol hoặc Terra công bố giá cache | Chạy lại mục 3.5; con số hiện dựa trên giả định |
| Gói đổi cách tính hạn mức, hoặc có số đo cách nó quy đổi token cache | Toàn bộ thứ tự ưu tiên, vì hiện xếp theo giá API |
| Bỏ hạn mức tuần riêng cho Fable, hoặc thêm hạn mức riêng cho model khác | Lợi ích của việc lead chạy Opus |
| Số đo một lượt làm việc mới cho thấy lead không còn chiếm phần lớn | Câu hỏi tier 4 cho builder |
| Thời hạn cache của host đổi khỏi một giờ | Nhịp 50 phút của giữ ấm |

## 9. Cách đo lại

Các script nằm ở `tools/usage/` trong thư mục này. Chúng chỉ in con số và nhãn việc, không in nội dung hội thoại. Giá được ghi cứng ở đầu mỗi script; sửa ở đó khi giá đổi.

Thay `<nhật ký>` bằng tệp `.jsonl` của phiên lead trong `C:\Users\phant\.claude\projects\<tên dự án>\`, và `<thư mục agent con>` bằng thư mục `subagents` cùng tên với phiên đó.

```bash
python -X utf8 tools/usage/usage_profile.py <nhật ký>
```

```bash
python -X utf8 tools/usage/usage_more.py <nhật ký>
```

```bash
python -X utf8 tools/usage/usage_agents.py <thư mục agent con>
```

```bash
python -X utf8 tools/usage/usage_activity.py <thư mục agent con> <mã agent 1> <mã agent 2>
```

```bash
python -X utf8 tools/usage/usage_tiers.py <thư mục agent con>
```

- `usage_profile.py`: chia chi phí phiên lead thành đọc, ghi, đầu ra; phân bố độ dài ngữ cảnh.
- `usage_more.py`: các lần ghi lớn (khởi động nguội), chi phí theo giờ. Giá ghi cứng là của Fable.
- `usage_agents.py`: tổng của từng agent con.
- `usage_activity.py`: chia chi phí builder theo loại hành động. Không tách được "viết test" khỏi "viết mã" khi builder sửa tệp bằng script.
- `usage_tiers.py`: phát lại các lượt gọi của builder theo giá có ngưỡng. Mã agent ghi cứng trong script; sửa khi đo lượt khác.

`AGENTS.md` toàn cục cấm đọc nhật ký của agent con. Chủ dự án đã cho phép chạy các script này ngày 15/11/2026 vì chúng chỉ cộng số. Lần sau cần hỏi lại.

## 10. Chưa đo và các giả định

- Gói Team quy đổi token cache ra phần trăm hạn mức thế nào. Phép thử ngày 15/11 không kết luận được vì công cụ trả về bản chụp và chỉ chính xác tới 1%.
- Chất lượng khi lead xuống Opus hoặc Sonnet, và khi builder xuống dưới Sonnet.
- Model rẻ cần thêm bao nhiêu lượt gọi cho cùng việc. Các bảng giả định bằng Sonnet, hoặc thêm 50%.
- Giá cache của Haiku, Sol và Terra.
- Ngưỡng tăng giá có tính cả phần đọc từ cache hay không; tôi tính là có.
- Chi phí riêng của việc viết test. Con số chắc chắn duy nhất là số dòng.
- Người viết test tách riêng có viết được bài bấm chuột thật của LH-ERP trước khi có giao diện hay không.
- Một chu kỳ giữ ấm nhiều giờ trên phiên lead Opus thật, và việc lần thức dậy có đọc từ cache hay không. Cơ chế hẹn giờ một-lần đã thử một lần và chạy đúng.
- QUICK_FIX chạy ở phiên rẻ (mục 3c) chưa chạy lần nào. Ngưỡng dưới của nó chưa đo: phiên mới tốn khoảng 58.000 token khởi động, có thể lớn hơn chính việc sửa một chữ.
- Tài liệu tham chiếu của Anthropic ghi rằng cách "rẻ trước, chạy lại phần lỗi ở mức cao hơn" giữ nguyên tỉ lệ đạt với hơn một nửa chi phí trong các lượt chạy lập trình của họ. Tôi chưa kiểm điều đó trên dự án này.
