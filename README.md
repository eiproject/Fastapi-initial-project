# Fastapi Start Ship

I've built a lightning-fast API using Python's coolest framework, FastAPI. It's like a sleek, customizable race car for your data. I've engineered it with a clean architecture, meaning the code is organized and easy to understand (even for non-engineers!). Think of it as building a house with a solid foundation – it's strong, flexible, and ready for anything. Let's see how fast we can make your ideas fly!

## Features

Your Start Ship's Core Features:

- **Blast Off with Authentication:** Securely launch your missions with our rock-solid register, login, and testing APIs.
- **Built-in Navigation:** Your ship comes equipped with FastAPI's docs for easy-to-use documentation.
- **Data Connections:** Power your journey with data from local or remote database using SQLAlchemy.
- **Secret Services:** Protect your valuable data with our JWT security shield.
- **Future-Proof Design:** Easily adapt to new missions with our flexible API versioning system.
- **Clean and Spacious Architecture:** Your ship is built for speed and customization with a clean design.
- **Engineer-Approved Blueprint:** We've followed the SOLID principles for a sturdy and reliable foundation.
- **Test Flight Ready:** Get started quickly with our pre-packed Postman toolkit.

## Project Architecture

```text
FastAPI-Start Ship
├── api
   ├── injection
      ... depedency injection
   ├── middleware
      ... api middleware
   ├── v1
      ├── form
         ... request form
      ├── repository
         ... implementation of repository
      ├── routes
         ... api routes
      ├── path.py
   ├── exception.py
   ├── routes.py
   ├── settings.py
├── core
   ├── dto
      ... application dto
   ├── model
      ... application related model
   ├── repository
      ... abstract class of repository
   ├── services
      ... application service
   ├── static
      ... static variable 
   ├── utils
      ... applciation utility
├── migrations
   ... yoyo and sql migration file
├── postman
   ... real case API test 
├── psql_db
   ├── model
      ... database model
   ├── settings.py
├ app.py
```

## Depedency

I am using `Python 3.12.3`, you may use lower or higher version of Python, but keep in mind to tune the library in `requirements.txt`

## That's All

Thanks you and best regards!
