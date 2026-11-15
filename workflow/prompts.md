# Version 4 entry - use one request

Claude Code after verified adapter installation:
```text
/dev <describe the intended correction or feature in your own language>
```
Codex: `$dev <request>`. Custom host: use its actually verified binding.
An empty entry resumes the active change; no active change means ask the goal.
The lead chooses QUICK_FIX / STANDARD / LARGE with risk and current-session scope.
Examples of intent: fix a broken filter; add branch-level export; plan a new
membership subsystem. 'Plan only' and 'verify only' remain read-only for product
code. No entry implicitly authorizes publish/merge/deploy.

For LARGE: approve the overall direction, then explicitly choose the milestone
for this session. For a clear QUICK_FIX: no second approval of the same repair is
needed; applicable edit/worktree permissions still apply.

Reusable-test cleanup: remove only scoped run data and eligible containers; keep
baseline, volumes, configuration and a usable startup recipe. Shared services
stay running unless separately authorized.

---

# Câu lệnh dùng hằng ngày

Dán vào chat của main agent, không chạy trong PowerShell.
Các chế độ dưới đây là yêu cầu bằng ngôn ngữ tự nhiên, không phải command mới của host.

## 1. Thiết lập lần đầu

```text
Đọc docs/agent-workflow/daily-workflow.md và skill dev-guardrails.
Tự kiểm tra repo và các công cụ hiện có để hoàn thiện project-setup.md.
Chỉ ghi nhận model, effort, cách gọi/resume worker đã xác minh.
Không tự cài dispatcher, thêm dịch vụ hoặc thay đổi CI.
Chỉ hỏi tôi những quyết định nghiệp vụ, chi phí, rủi ro hoặc quyền còn thiếu;
kèm bối cảnh, phương án, đánh đổi, rủi ro và khuyến nghị.
Chưa sửa code sản phẩm.
```

## 2. Bắt đầu hoặc tiếp tục

```text
Theo docs/agent-workflow/daily-workflow.md và skill dev-guardrails,
tiếp tục change đang làm từ checkpoint trong repo.
Xác minh workspace thực tế trước; không lập lại spec hoặc hỏi lại quyết định đã chốt.
Mặc định main review, builder cũ test và fix; không tạo swarm.
Các change không đụng nhau được chạy song song, mỗi change một worktree.
Làm trong phạm vi đã duyệt và các quyền đã cấp.
Dừng ở READY_FOR_PR hoặc BLOCKED; không merge/deploy.
Trước khi sửa, tạo hoặc tiếp tục worktree riêng của change.
Không dev trực tiếp trên main; dùng lại worktree qua các vòng fix.
```

## 3. Feature mới

```text
Theo daily-workflow.md, lập kế hoạch cho: [nhu cầu của tôi].
Tự đọc hiện trạng; chỉ hỏi các quyết định có ảnh hưởng thật.
Mỗi câu hỏi cần có bối cảnh, phương án, đánh đổi, rủi ro và lời khuyên.
Tạo spec gọn, AC và task theo hành vi hoàn chỉnh để tôi duyệt chung.
Chưa implement những quyết định quan trọng chưa được duyệt.
```

## 4. Duyệt và build

```text
Tôi duyệt phạm vi, quyết định và AC trong [change record / revision].
Hãy implement với TDD, review và fix theo daily-workflow.md.
Được sửa code/test trong phạm vi này và chạy kiểm tra local an toàn.
Được commit cục bộ trên nhánh của change.
Chưa push, tạo PR, merge hay deploy nếu chưa có quyền riêng.
Trước READY_FOR_PR, cho tôi xem kết quả chạy thật: các bước bấm thử kèm ảnh chụp.
```

## 5. Chỉ verify

```text
Verify-only [change record] trên candidate hiện tại theo daily-workflow.md.
Đối chiếu từng AC, code liên quan và bằng chứng thật.
Tái sử dụng kết quả còn hiệu lực; chỉ chạy bù phần thiếu/bị ảnh hưởng.
Không sửa sản phẩm, không audit lại toàn repo.
Trả READY_FOR_PR, NEEDS_WORK hoặc BLOCKED với lý do và bằng chứng.
```

## 6. Kết thúc phiên

```text
Kết thúc tại đây. Cập nhật checkpoint trong change record hiện tại.
Ghi phase/task, candidate, worker/session thật, evidence, blocker
và một bước tiếp theo cụ thể. Không sao chép toàn bộ chat.
Báo rõ cái gì chưa verify và process nào vẫn đang chạy.
Không để worker sửa code hoặc dịch vụ test chạy tiếp ngoài ý muốn.
```

## 7. Lập kế hoạch release, chưa thực thi

```text
Dùng release-housekeeping và docs/agent-workflow/release-workflow.md.
Lập kế hoạch release cho change đã duyệt hiện tại.
Kiểm tra trigger push/merge, CI, phần cần deploy, migration và thứ tự an toàn.
Liệt kê worktree, branch và tài nguyên test sẽ dọn sau khi deploy thành công.
Giải thích rủi ro quan trọng và khuyến nghị. Chưa publish/deploy/xóa.
```

## 8. Thực thi release đã duyệt

```text
Tôi duyệt kế hoạch release trong [record/revision] cho [repo/môi trường].
Thực hiện PR, merge về origin/main, deploy/migration cần thiết,
kiểm tra sau deploy, fast-forward local main an toàn và housekeeping trong scope.
Tái sử dụng CI/platform hiện có; không deploy/migration hai lần.
Dừng khi phát sinh scope mới, gate fail hoặc dữ liệu không rõ.
Không hard reset, prune Docker toàn host, xóa test source/volume chung.
Báo kết quả từng bước và phần housekeeping còn vướng.
```

## 9. Tiếp tục release dở dang / chỉ dọn dẹp

```text
Tiếp tục release record tại [đường dẫn]. Xác minh trạng thái PR,
deploy và migration thực tế; không chạy lại thao tác đã hoàn thành/chưa rõ.
Nếu chỉ còn housekeeping thì không redeploy. Giữ logs và tài nguyên chung,
báo RELEASED_CLEANUP_PENDING khi chưa thể hoàn tất an toàn.
```
