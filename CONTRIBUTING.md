# Contributing Guidelines

## Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages. This leads to more readable messages that are easy to follow when looking through the project history.

### Commit Message Format

Each commit message consists of a **header**, a **body** and a **footer**. The header has a special format that includes a **type**, a **scope** and a **subject**:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The **header** is mandatory and the **scope** of the header is optional.

### Type

Must be one of the following:

* **feat**: A new feature
* **fix**: A bug fix
* **docs**: Documentation only changes
* **style**: Changes that do not affect the meaning of the code (white-space, formatting, etc)
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **perf**: A code change that improves performance
* **test**: Adding missing tests or correcting existing tests
* **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation

### Scope

The scope should be the name of the module affected (as perceived by the person reading the changelog generated from commit messages).

### Subject

The subject contains a succinct description of the change:

* use the imperative, present tense: "change" not "changed" nor "changes"
* don't capitalize the first letter
* no dot (.) at the end

### Body

Just as in the **subject**, use the imperative, present tense. The body should include the motivation for the change and contrast this with previous behavior.

### Footer

The footer should contain any information about **Breaking Changes** and is also the place to reference GitHub issues that this commit **Closes**.

### Examples

```
feat(models): add new staging model for GTFS routes

* Create stg_routes.sql
* Add route_type mapping
* Include agency reference

Closes #123
```

```
fix(pipeline): correct CSV download path

The CSV download path was incorrectly pointing to a temporary directory.
Now uses the configured data/raw directory.

Closes #456
```

```
docs(readme): update development setup instructions

* Add Poetry installation steps
* Clarify Docker requirements
* Update troubleshooting section
```

## Pull Request Process

1. Create a feature branch from `main`
2. Follow the conventional commits specification for all commits
3. Update documentation as needed
4. Open a pull request with a clear description of the changes
5. Ensure all checks pass
6. Request review from maintainers
