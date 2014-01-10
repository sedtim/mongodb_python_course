db.posts.aggregate([
  {$unwind:"$comments"},
  {$project:{_id:0, comments:1}},
  {$group:{_id:"$comments.author", num_comments:{$sum:1}}},
  {$sort:{num_comments:1}},
])


db.zips.aggregate([
  {$match:{$or:[{"state":"CA"}, {"state":"NY"}]}},
  {$group:{_id:{city:"$city", state:"$state"}, "pop":{$sum:"$pop"}}},
  {$match:{"pop":{$gt:25000}}},
  {$group:{_id:"CA & NY", avg_pop:{$avg:"$pop"}}}
])

db.grade.aggregate([
  {$unwind:"$scores"},
  {$match:{"scores.type":{$ne:"quiz"}}},
  {$group:{_id:{sid:"$student_id", cid:"$class_id"}, "avg_score":{$avg:"$scores.score"}}},
  {$group:{_id:"$_id.cid", "average":{$avg:"$avg_score"}}},
  {$sort:{average:1}}
])

db.zips.aggregate([
  {$project:{fc:{$substr:["$city",0,1]}, pop:"$pop"}},
  {$match:{"fc":{$gte:"0", $lte:"9"}}},
  {$group:{_id:"Living in a zip code", "sum_pop":{$sum:"$pop"}}}
])
