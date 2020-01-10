FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN yarn
COPY . .
# All of these below are for production mode, comment all of them while using for development mode
#RUN npm run build


# Production stage
#FROM nginx as production-stage
#RUN mkdir /app
#COPY --from=build-stage /app/dist /app
#EXPOSE 80
#COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

