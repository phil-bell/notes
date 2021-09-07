# Libraries causing warnings
- `django-axes`
- `django-cron`
- `django-filter`
- `django-formtools`
- `django-froala-editor`
- `django-hosts`
- `django`
- `Markdown`
- `rest-framework-generic-relations`
## Libraries we can update
- `django-formtools` `1.0` -> `2.3`
- `django-froala-editor` `2.9.5` -> `3.2.2`
- `Markdown` `3.3.3` -> `3.3.4`


## result of upgrade
- django-axes `5.2.2` -> `5.21.0`
  - fixed it ✅
- `django-formtools` `1.0` -> `2.3`
  - fixed it ✅
- `django-froala-editor` `2.9.5` -> `3.2.2`
  - no affect and caused issues, rolled back to `2.9.5`
- `Markdown` `3.3.3` -> `3.3.4`
  - no affect
## Libraries without update

- `django` `<4`
- `django-cron` `0.5.1`
- `django-filter` `2.4.0`
- `django-hosts`
- `rest-framework-generic-relations` `^2.0.0`
