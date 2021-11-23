# Heroku CLI

## Useful commands

### Cancel a deploy
```bash
heroku builds:cancel -a APP_NAME

heroku builds:cancel -a legl-review-pr-7499
```

### SSH into a dyno
```bash
heroku ps:exec -a APP_NAME
heroku ps:exec -a legl-review-pr-7381
```

### Connect to apps database
```bash
heroku pg:psql DB_NAME --app APP_NAME
heroku pg:psql postgresql-angular-31308 --app crowdjustice-production
```

### Tail an apps logs
```bash
heroku logs -a APP_NAME -t
heroku logs -a legl-review-pr-7381 -t
```

### Get last n logs
```bash
heroku logs -a DB_NAME -n LINES
heroku logs -a legl-review-pr-7381 -n 10000
```
