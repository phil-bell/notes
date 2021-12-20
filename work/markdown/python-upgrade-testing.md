# Python upgrade

## Rollout Plan
### Monitoring
- sentry
- Papertrail
- Metabase
- CloudAMQ (RabbitMQ)
- Revenue monitoring (ask toby)

### Testing
- Running cypress tests 10+ times (review or stage)
- Test PDFs render as expected (review)
- Test several background tasks work as expected (stage)
  - worker and slowworker
- Test Styling hasn't changed from sass library upgrades (review)
  - Try Chrome, Firefox, Safari, all desktop and mobile

### Reaction tree
1. Everything is good
   1. No action needed
2. Hit a snag
   1. fix forwards
   2. rollback dyno
   3. rollback database

### Areas of concern
- `PyMuPDF`
  - PDFs wont render at all or will small alterations
- `gunicorn`
  - if theres an issue will likely just bring down entire site
- `celery`
  - If failed background tasks wont run
- `icon-font-generator`
  - Icon wont render
- `node-sass` and `gulp-sass`
  - Styling wont transpile

### Questions
- Can we remove `jsmin`
- Can we remove `Ne Relic

