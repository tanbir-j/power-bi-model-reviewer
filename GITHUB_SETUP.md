# Private GitHub setup

## Recommended ownership

Create the repository inside a GitHub organisation when you want selected people to have different permission levels. Use a personal private repository only when every collaborator can safely receive write access.

Suggested repository name:

`power-bi-model-reviewer`

Suggested description:

`Cross-platform GPT and Claude skill for documenting, reviewing and improving Power BI solutions.`

Do not initialise the remote repository with a README, licence or `.gitignore`; these files already exist locally.

## Create the repository

1. In GitHub, choose **New repository**.
2. Select the organisation owner.
3. Enter `power-bi-model-reviewer`.
4. Select **Private**.
5. Leave README, `.gitignore` and licence unchecked.
6. Create the repository.

## Push this folder

From a terminal opened in this folder:

```bash
git init
git add .
git commit -m "Initial private release of Power BI Model Reviewer"
git branch -M main
git remote add origin https://github.com/ORGANISATION/power-bi-model-reviewer.git
git push -u origin main
```

Replace `ORGANISATION` with the GitHub organisation or account name.

GitHub may ask you to authenticate through the browser, GitHub Desktop, a personal access token, or SSH.

## Give selected people access

1. Open the repository.
2. Choose **Settings**.
3. Under **Access**, open **Collaborators & teams**.
4. Choose **Add people** or **Add teams**.
5. Select the lowest suitable role:
   - **Read** for reviewers and users;
   - **Triage** for issue management without source changes;
   - **Write** for contributors;
   - **Maintain** for project maintainers;
   - **Admin** only for repository owners.
6. Review access periodically and remove it when no longer required.

## Recommended protection

After the first push:

- protect the `main` branch;
- require a pull request before merging;
- require at least one approval;
- prevent force pushes and deletion;
- restrict who can push directly to `main`;
- enable secret scanning and Dependabot where available;
- disable private-repository forking if your organisation policy requires it;
- replace `@USERNAME` in `.github/CODEOWNERS`.

## Releases

Use source tags such as `v0.2.0`. Attach the validated `skill.zip` to the GitHub release so users can download the packaged skill without cloning the repository.
