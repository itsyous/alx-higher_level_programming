-- list all genres from hbtn_0d_tvshows along
SELECT g.'name' AS 'genre',
       COUNT(*) AS 'number_of_shows'
  FROM 'tv_genres' AS g
       INNER JOIN 'tv_shows_genres' AS t
       ON g.'id' = t.'genre_id'
 GROUP BY g.'name'
 ORDER BY 'number_of_shows' DESC;
