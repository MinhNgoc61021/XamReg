FROM node:lts-alpine
WORKDIR /usr/src/app
COPY package.json .
RUN npm install
COPY . .
#RUN npm run build


## Production stage
#FROM nginx:1.16.1-alpine as production-stage
#COPY --from=build-stage /app/dist /usr/share/nginx/html
#EXPOSE 80
## Here we can serve the Vue app using port 80, however it runs port 8001 on PC and 80 in the container
#CMD [ "nginx", "-g", "daemon off;"]
