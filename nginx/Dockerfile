# This image will contain the JS code as well since it's nginx serving it.
# Using multi-stage docker build for a smaller final image.
FROM node:9.5 AS jsbuilder

WORKDIR ./client
COPY ./client ./client


RUN npm install
RUN npm run build

# Multi-stage means the build context needs to be the same, that's a bit disappointing (coupling!)...
FROM nginx:1.13.9-alpine

COPY ./nginx/nginx.conf ./etc/nginx/nginx.conf

COPY --from=jsbuilder /client/dist/ app/