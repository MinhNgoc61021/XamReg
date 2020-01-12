FROM node:lts-alpine as build-stage
RUN npm install --quiet --global vue-cli@2.9.3

RUN mkdir /app

WORKDIR /app
COPY package*.json ./
RUN yarn
COPY . .


