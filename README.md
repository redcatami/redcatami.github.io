# Redcatech

A custom Jekyll portfolio for redcatami, built for GitHub Pages. No WordPress, public registration, passwords, or browser-based publishing endpoint. Visitors can read the site; only people authorized to change your GitHub repository can publish changes.

## Publish to GitHub Pages

1. Create a repository named **redcatami.github.io** under your GitHub account. Do not overwrite an existing repository.
2. Upload the site source files, including the `.github/workflows` directory. Do not upload `.tools`, `vendor`, `_site`, or credentials.
3. Set the default branch to `main`.
4. Open **Settings → Pages** and choose **GitHub Actions** as the build source.
5. Run **Build and deploy Redcatech** in Actions, or push a change to `main`.
6. After deployment succeeds, your site will be at `https://redcatami.github.io`.

The workflow also supports project repositories: it gets the correct base path from GitHub Pages. If you use a different repository name, its published address will include that name.

## Make it yours

- Edit `_data/profile.yml` for your name, introduction, biography, and social URLs. Blank social URLs display as “Coming soon” and do not create misleading links.
- Edit `about.html` for your personal story. The initial prose is editable introductory copy, not a verified biography.
- Add career entries to `career` in `_data/profile.yml`:

```yaml
career:
  - period: "2024–present"
    title: "Your role"
    company: "Your employer"
    description: "Your responsibilities and achievements."
```

- Copy `examples/project.md` to `_projects/project-name.md`, replace the sample fields, and commit. Create `_projects` if needed.
- Copy `examples/article.md` to `_posts/YYYY-MM-DD-article-name.md`, replace the content, and commit. Create `_posts` if needed. Use a past or current date; future posts are not published automatically.
- Add screenshots to `assets/images/` and set `image` and `image_alt` on the project. Avoid putting private data in screenshots.
- Draft articles can live in `_drafts/` and are omitted from the published site. A public GitHub repository still exposes their source, so do not store confidential drafts there.
- Set `published: false` in a project or post to omit it from the site. Its source remains visible if the repository is public.

No fictional projects, jobs, or social accounts have been published. The empty portfolio and journal states are intentional until you add real content.

## Local development

Install Ruby 3.3 and Bundler, then run:

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

Open `http://127.0.0.1:4000`. Restart Jekyll after changing `_config.yml`.

Production build:

```sh
JEKYLL_ENV=production bundle exec jekyll build
```

On PowerShell, use `$env:JEKYLL_ENV='production'` before the build command.

## Account security

Use a passkey or two-factor authentication on GitHub, avoid unnecessary repository collaborators, and never commit tokens or credentials. There is no public form that allows visitors to create projects or posts. Static hosting does not process untrusted submissions. Markdown is trusted author content, so review contributions before merging.

The GitHub Actions workflow grants deployment permission only to its automation token. The local site is prepared; it is not live until uploaded and its deployment succeeds.
