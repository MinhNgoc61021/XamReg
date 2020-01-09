# This image will contain the JS code as well since it's nginx serving it.
# Using multi-stage docker build for a smaller final image.
FROM node:lts AS jsbuilder

WORKDIR /app
COPY . .

RUN npm install

# Multi-stage means the build context needs to be the same, that's a bit disappointing (coupling!)...
FROM nginx:1.13.9-alpine
WORKDIR /app
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY --from=jsbuilder app/dist /usr/share/nginx/html

