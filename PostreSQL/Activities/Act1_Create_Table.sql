CREATE TABLE public.product_a (
	id int4 NOT NULL,
	prodname varchar NOT NULL,
	prodprice numeric NOT NULL,
	CONSTRAINT product_a_pk PRIMARY KEY (id)
);

INSERT INTO public.product_a
(id, prodname, prodprice)
values
(001, 'Laptop', 30000.50),
(002, 'Television', 123500.55),
(003, 'Aircon', 32467.557);