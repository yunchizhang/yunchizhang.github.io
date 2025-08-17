Title: Synchronizing Multiple Remote Repositories
Date: 2025-8-17 11:08
Category: Coding
Tags: repository, git, remote
Slug: multi_remote_repos
Authors: Yunchi Zhang
Summary: How to synchronize multiple remote repositories with a local one.
Keywords: Git, Repository

[TOC]

## Multiple Remote Git Repositories

Synchronizing two remote Git repositories is often needed if, for example, you’re mirroring between
[GitHub](https://github.com) and [GitLab](https://gitlab.com), or keeping a company’s internal Git server in sync with
a public one. There are several approaches depending on you needs. The following workflow is an example of having two
repositories (say GitHub + GitLab, or company server + external host) that both accept pushes, and developers might
push to either.

That's what I'd call a *collaborative multi-remote workflow*. The steps are:

### 1. Add Both Remotes

Suppose you cloned from server A:

```bash
git clone git@serverA:user/repo.git
cd repo
```

Now add server B:

```bash
git remote add serverB git@serverB:user/repo.git
```

You’ll now have:

* **origin** → server A
* **serverB** → server B

Check with:

```
git remote -v
```

### 2. Keeping Both in Sync

Since developers may push to either, you’ll want to *fetch and merge/rebase* changes from both regularly:

```bash
# Fetch all branches from both
git fetch origin
git fetch serverB
```

Now, update your local branch:

```bash
git checkout main
git pull origin main
git pull serverB main
```

That merges in changes from both sides.
Then push back to both:

```bash
git push origin main
git push serverB main
```

### 3. Avoiding Divergence

If people are working on feature branches, do the same process:

```bash
git checkout feature-x
git pull origin feature-x
git pull serverB feature-x
git push origin feature-x
git push serverB feature-x
```

If there are conflicts, you’ll resolve them locally and push the resolved history to both remotes.

### 4. Automating Multi-Push

You can configure Git so one push command updates both:

```bash
git remote set-url --add --push origin git@serverA:user/repo.git
git remote set-url --add --push origin git@serverB:user/repo.git
```

Now:

```bash
git push origin main
```

will push to both A and B.

But pulls are still separate — you’ll need to git pull from both remotes, because Git doesn’t merge multiple fetches
automatically.

### 5. Best Practices

* Decide on a primary remote for coordination (e.g., GitHub). Pull from both, but if conflicts arise, resolve and push to both.

* Use branch protection rules on both servers if you want consistent workflow (reviews, CI/CD, etc.).

* Consider a CI job or hook to auto-sync branches (e.g., GitHub Action that pushes to GitLab). That way developers only need to push once.