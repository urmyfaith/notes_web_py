CREATE TABLE todo (
  id serial primary key,
  title text,
  created timestamp default now(),
  done boolean);