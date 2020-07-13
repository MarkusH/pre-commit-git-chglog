# pre-commit-git-chglog

This is a [pre-commit](https://pre-commit.com/) hook that ensures a commit message
adheres to the [git-chglog](https://github.com/git-chglog/git-chglog) requirements.

For this hook to work, the following settings need to be defined in the `.chglog/config.yml`.
The values for `options.commits.filters.Type`, `options.header.pattern`, and
`options.header.pattern_maps` do not matter. However, `pattern_maps` must contain
`Type` and its position within that list represents the match group within the
pattern that it will be looked up in.

```yaml
options:
  commits:
    filters:
      Type:
        - chg
        - feat
        - fix
        - perf
        - ref
        - docs
        - pkg
  header:
    pattern: "^(\\w*)\\:\\s(.*)$"
    pattern_maps:
      - Type
      - Subject
```

`.pre-commit-config.yaml`:

```yaml
repos:
- repo: https://github.com/MarkusH/pre-commit-git-chglog
  rev: master
  hooks:
  - id: git-chglog
    stages: [commit-msg]
```
