BIS='https://www.bis.gov/media/documents/guidelines-preparing-export-license-applications-involving-foreign-persons'
DOJ='https://www.justice.gov/crt/media/1287536/dl'
pages={
'zh':[
('offer-review','芯片公司 offer 要等出口许可证，入职日期怎么定？','从 offer 中找出出口许可（EL）条件，区分申请准备、已提交和等待结果，并向招聘方确认最晚入职日。',[
('先确认进度','招聘人员说“在等 EL”时，可以问公司目前是在确认是否需要申请，还是已经向主管部门提交申请。请对方区分岗位评估、材料准备和等待决定三个阶段。'),
('弄清许可涉及什么','请招聘人员把问题转给公司的出口合规团队。可以提供公开的岗位说明，由公司确认涉及的技术、适用法规及是否有可用授权。个人不必根据“芯片工程师”这个职位名称自行推断。'),
('把下一步落实到日期','向招聘方确认 offer 的截止日、下一次进度更新的日期，以及如果许可届时仍在审理，公司是否能调整入职时间。开工日期以雇主书面确认为准。')],[(BIS,'美国商务部 BIS · 视同出口申请指南')]),
('recruiter-questions','Export License 申请卡住，怎么用英文问 HR 进度？','用一封英文邮件向招聘方确认申请是否已提交、是否需要补材料，以及下一次更新时间。',[
('先问岗位','“Which responsibilities or technologies in this role may require an export license?” 请对方说明需要评估的是哪部分工作职责。只讨论公开的岗位范围。'),
('再问申请材料','“Which documents do you need from me, and how should I send them?” 请招聘方列出还缺哪些材料，并确认提交渠道。'),
('最后问进度','“Has the company submitted an export license application for this role yet? When should we check in again about my start date?” 留存对方的回复和下一次跟进日期。')],[(BIS,'BIS · 申请材料与技术说明'),(DOJ,'美国司法部 · 出口合规评估与工作资格核验')])],
'en':[
('offer-review','How does an export license condition affect a semiconductor job offer?','Read the condition in your offer, establish whether the employer has filed an application and agree on a start date or a check-in date.',[
('Find out where the review stands','When a recruiter says an offer is waiting on an export license, ask whether the company is assessing the role, preparing an application or waiting for a government decision. Each stage has a different next step.'),
('Identify the access involved','Share the public job description with recruiting. Ask the employer’s export compliance team to confirm the relevant technology, applicable rules and any authorization that covers the proposed access. A chip design job title alone cannot settle the question.'),
('Agree on a follow-up date','Ask when the offer expires, when the team will update you and whether the start date can move if the review continues. Use the employer’s written confirmation when planning your start date.')],[(BIS,'BIS guidance on deemed export applications')]),
('recruiter-questions','How to ask a recruiter about an export license delay','An English follow-up email for semiconductor candidates waiting on an export license. Ask about filing status, outstanding documents and your start date.',[
('Ask about responsibilities','“Which responsibilities or technologies in this role may require an export license?” Keep the conversation at the level of the public job description.'),
('Ask about documentation','“Which documents do you need from me, and how should I send them?” Ask for a list of outstanding items and the preferred way to submit them.'),
('Ask about timing','“Has the company submitted an export license application for this role yet? When should we check in again about my start date?” Keep a copy of the answer and the agreed follow-up date.')],[(BIS,'BIS · Deemed export application requirements'),(DOJ,'U.S. Department of Justice · Export compliance assessments')])]}

LICENSING = 'https://www.bis.gov/licensing'
pages['zh'].extend([
    ('application-status', '美国出口许可提交后，怎样查 BIS 申请进度？',
     '弄清是谁提交了申请、哪一天提交，以及雇主能从 SNAP-R 或 STELA 查到什么。', [
        ('先确认是否已经提交', '如果 HR 只说“在办 EL”，先问负责申请的团队是否已向美国商务部工业与安全局（BIS）提交，以及提交日期。公司内部收齐材料的日期和向 BIS 提交的日期可能不同。'),
        ('由提交方核对官方记录', '在 BIS 的许可页面，Apply for a license 指向提交申请的 SNAP-R，Track an application 提供 STELA 状态查询入口。若申请是雇主提交的，请其合规团队核对记录，再告诉你最近一次更新的日期和是否需要你补材料。'),
        ('把申请进度和报到日期分别记下来', '可以这样记录招聘方的回复：“申请已于［日期］提交；目前需补交［材料或无］；公司将在［日期］再次确认能否按时报到。”最终开工日期向招聘方书面确认。')
     ], [(LICENSING, 'BIS · 提交申请与查询状态的官方入口')]),
    ('application-documents', '芯片工程师申请美国出口许可，要准备哪些材料？',
     '按 BIS 的视同出口申请指南整理证件、履历和研究经历，并与雇主确认提交方式。', [
        ('先核对证件和提交渠道', 'BIS 指南列出清晰有效的护照、签证和工作授权文件。先请公司合规团队列出适用于你的材料和上传入口。按对方要求分别准备文件，核对有效期。'),
        ('整理教育、工作和研究履历', '按时间列出学校、就读日期、学位、历任雇主和工作职责，说明经历中的空档。做过研究或发表过文章的，可以另列项目简介、文章题目、发表日期及刊物，供雇主核对。'),
        ('向公司确认岗位说明由谁准备', 'BIS 指南还列有解释信（Letter of Explanation）。向合规团队确认由谁说明岗位涉及的技术和接触范围。你可以先准备岗位名称、公开的职位描述及履历；证件通过公司指定渠道提交。')
     ], [(BIS, 'BIS · 涉及外国人员的许可申请指南，第 II、IV、V 节')]),
])
pages['en'].extend([
    ('application-status', 'How to check the status of a U.S. export license application',
     'Find out who filed the application, when it was submitted and how the employer can check for updates through BIS.', [
        ('Confirm the filing date', 'If recruiting says your license is in progress, ask whether the filing team has submitted it to the Bureau of Industry and Security (BIS) and on what date. The team may have finished collecting your documents before it filed.'),
        ('Ask the filing team to check the official record', 'The BIS licensing page links to SNAP-R under Apply for a license and to STELA under Track an application. If your employer filed the application, ask its compliance team to check the record and tell you when the status last changed and whether it needs anything from you.'),
        ('Record the next hiring decision separately', 'A useful update reads, “Filed on [date]. Outstanding documents: [items or none]. Recruiting will revisit the start date on [date].” Ask recruiting to confirm the eventual start date in writing.')
     ], [(LICENSING, 'BIS · Official application and status tools')]),
    ('application-documents', 'Documents for a semiconductor deemed export license application',
     'Use BIS guidance to prepare identity documents and an accurate work and research history, then confirm how your employer wants to receive them.', [
        ('Check the documents and the submission channel', 'BIS guidance lists legible, valid copies of the passport, visa and work authorization. Ask the compliance team which documents apply to your circumstances and where to upload them. Check expiration dates and prepare separate files as requested.'),
        ('Build a timeline of education, work and research', 'List schools, attendance dates, degrees, employers and duties in chronological order. Explain gaps. For research and publications, collect short project descriptions, article titles, publication dates and journal names so the employer can check the details.'),
        ('Agree on who will describe the role', 'The BIS guidance also calls for a Letter of Explanation. Ask compliance who will describe the technology involved and the access the role requires. Have your job title, public job description and résumé ready, and use the company’s designated channel for identity documents.')
     ], [(BIS, 'BIS · Foreign-person application guidance, sections II, IV and V')]),
])
