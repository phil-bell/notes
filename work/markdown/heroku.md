# Heroku CLI

## Useful commands

### Cancel a deploy
command:
```bash
heroku builds:cancel -a APP_NAME
```
example:
```bash
heroku builds:cancel -a legl-review-pr-7499
```

### SSH into a dyno
command:
```bash
heroku ps:exec -a APP_NAME
```
example:
```bash
heroku ps:exec -a legl-review-pr-7381
```

### Connect to apps database
command:
```bash
heroku pg:psql DB_NAME --app APP_NAME
```
example:
```bash
heroku pg:psql postgresql-angular-31308 --app crowdjustice-production
```

### Tail an apps logs
command:
```bash
heroku logs -a APP_NAME -t
```
example:
```bash
heroku logs -a legl-review-pr-7381 -t
```

### Get last n logs
command:
```bash
heroku logs -a DB_NAME -n LINES
```
example:
```bash
heroku logs -a legl-review-pr-7381 -n 10000
```
