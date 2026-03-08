select strftime(ts, '%Y-%m-%dT%H:00') as bucket, sum(value) as bucket_sum from series group by 1 order by 1;
