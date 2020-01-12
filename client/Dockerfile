FROM node:lts-alpine as build-stage
RUN mkdir /client
WORKDIR /client
COPY package.json .
RUN npm install
COPY . .
# All of these below are for production mode, comment all of them while using for development mode
RUN npm run build

# Production stage
FROM nginx:1.13.9-alpine as production-stage
COPY --from=build-stage /client/dist/ /app
CMD [ "nginx", "-g", "daemon off;" ]
