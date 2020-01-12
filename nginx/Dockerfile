# Build stage
FROM node:lts-alpine as build-stage
COPY /client /client
WORKDIR /client
RUN yarn
RUN npm run build
# All of these below are for production mode, comment all of them while using for development mode

# Production stage
FROM nginx:1.13.9-alpine as production-stage
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=build-stage /client/dist app/
CMD [ "nginx", "-g", "daemon off;" ]