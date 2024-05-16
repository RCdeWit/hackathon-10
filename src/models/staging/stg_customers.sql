WITH

source AS (
	SELECT * FROM {{ source('raw_space_fuel_shop', 'public_customers') }}
),

renamed AS (
	SELECT
		"ID" AS customer_id,
		"FIRST_NAME" AS first_name,
	FROM source
)

SELECT * FROM renamed
