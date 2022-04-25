/* Legacy SQL */

SELECT
  /* Replace underscores in the title with spaces  */
  REGEXP_REPLACE(title, r' ', ' ') AS regexp_title, views
  FROM
    (SELECT title, SUM(views) as views 
    FROM [bigquery-samples:wikipedia_benchmark.Wiki100M]
  WHERE
    NOT title CONTAINS ':'
    AND wikimedia_project='wp'
    AND language='en'
    /* Match titles that start with 'G', */
    /* end with 'e', and contain two 'o's  */
    AND REGEXP_MATCH(title, r'^G.*o.*o.*e$')
  GROUP BY
    title
  ORDER BY
    views DESC
  LIMIT 100)
