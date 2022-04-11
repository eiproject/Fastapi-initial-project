# Fastapi-initial-project

Fastapi is a strength and efficient API framework in Python, used widely as a standalone service. With a lot of customization and flexibility peoples choose fastaip as their backend. This project is my own taste for Fastapi, conneted to some books that I read about coding principle. This code architecture maybe not your type, so you are freely to suggest me about what suit better.

## Features

This is a startship project which have several features as default:

- Register, Login, and User lookup API
- Integrated with fastapi default Docs
- Local and remote database connection using sqlalchemy
- JWT security on the middleware
- Code friendly on API versioning
- Good architecture for code expansion and customization based on SOLID principle

## Project Architecture

```text
Fastapi-initial-project
├── core
   ├── forms
      ├── login_form.py
      ├── register_form.py
   ├── models
      ├── token_data.py
      ├── token.py
      ├── user.py
   ├── __init__.py
   ├── settings.py
├── db
   ├── contexts
      ├── context_user.py
   ├── __init__.py
   ├── credentials.py
   ├── models.py
   ├── settings.py
├── tests
   ├── v1
      ├── __init__.py
      ├── test1.py
   ├── __init____.py
├── v1
   ├── endpoints
      ├── __init__.py
      ├── endpoint_common.py
      ├── endpoint_user.py
   ├── services
      ├── service_user.py
   ├── __init___.py
   ├── middleware_user.py
   ├── routes.py
├ main.py
├ test.py
```

## End

Thanks for your attention. Regards.
