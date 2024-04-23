CREATE TABLE "User" (
  "id" SERIAL PRIMARY KEY,
  "first_name" VARCHAR NOT NULL,
  "last_name" VARCHAR NOT NULL,
  "phone" VARCHAR UNIQUE NOT NULL,
  "email" VARCHAR UNIQUE NOT NULL,
  "password" VARCHAR NOT NULL
);

CREATE TABLE "Boxpackage" (
  "id" SERIAL PRIMARY KEY,
  "count_container" INTEGER NOT NULL,
  "size" VARCHAR NOT NULL,
  "location" VARCHAR UNIQUE NOT NULL
);

CREATE TABLE "Container" (
  "id" SERIAL PRIMARY KEY,
  "fk_boxpackage_id" INTEGER REFERENCES "Boxpackage" ("id"),
  "number" INTEGER UNIQUE NOT NULL,
  "capacity" VARCHAR NOT NULL
);

CREATE TABLE "Package" (
  "id" SERIAL PRIMARY KEY,
  "number" INTEGER UNIQUE NOT NULL,
  "pin" INTEGER NOT NULL,
  "status" VARCHAR NOT NULL
);

CREATE TABLE "Delivery" (
  "id" SERIAL PRIMARY KEY,
  "fk_package_number" INTEGER UNIQUE REFERENCES "Package" ("number"),
  "fk_from_container_num" INTEGER REFERENCES "Container" ("number"),
  "fk_to_container_num" INTEGER REFERENCES "Container" ("number"),
  "fk_from_boxpackage_location" VARCHAR REFERENCES "Boxpackage" ("location"),
  "fk_to_boxpackage_location" VARCHAR REFERENCES "Boxpackage" ("location"),
  "fk_user_id" INTEGER REFERENCES "User" ("id"),
  "data_departure" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "data_receiving" TIMESTAMP NOT NULL
);

CREATE INDEX ON "Delivery" ("fk_user_id");

ALTER TABLE "Container" ADD CONSTRAINT fk_container_boxpackage FOREIGN KEY ("fk_boxpackage_id") REFERENCES "Boxpackage" ("id");

ALTER TABLE "Delivery" ADD CONSTRAINT fk_delivery_package FOREIGN KEY ("fk_package_number") REFERENCES "Package" ("number");

ALTER TABLE "Delivery" ADD CONSTRAINT fk_delivery_from_container FOREIGN KEY ("fk_from_container_num") REFERENCES "Container" ("number");

ALTER TABLE "Delivery" ADD CONSTRAINT fk_delivery_to_container FOREIGN KEY ("fk_to_container_num") REFERENCES "Container" ("number");

ALTER TABLE "Delivery" ADD CONSTRAINT fk_delivery_from_boxpackage FOREIGN KEY ("fk_from_boxpackage_location") REFERENCES "Boxpackage" ("location");

ALTER TABLE "Delivery" ADD CONSTRAINT fk_delivery_to_boxpackage FOREIGN KEY ("fk_to_boxpackage_location") REFERENCES "Boxpackage" ("location");

ALTER TABLE "Delivery" ADD CONSTRAINT fk_delivery_user FOREIGN KEY ("fk_user_id") REFERENCES "User" ("id");

ALTER TABLE "Login" ADD CONSTRAINT fk_login_user FOREIGN KEY ("fk_user_id") REFERENCES "User" ("id");