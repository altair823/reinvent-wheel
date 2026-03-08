select team, sum(amount) as total, count(*) as row_count from sales where status = 'ok' group by team order by team;
