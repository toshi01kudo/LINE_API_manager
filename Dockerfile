FROM node:16-alpine3.15
RUN mkdir /app
WORKDIR /app
COPY ./app/package.json /app/

RUN yarn install
ENTRYPOINT ["yarn", "dev"]
