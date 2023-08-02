migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("dv6hi1xylwqfrv1")

  collection.listRule = "@request.auth.id != \"\" && user = @request.auth.id"
  collection.viewRule = "@request.auth.id != \"\" && user = @request.auth.id"
  collection.createRule = "@request.auth.id != \"\" && user = @request.auth.id"
  collection.updateRule = "@request.auth.id != \"\" && user = @request.auth.id"
  collection.deleteRule = "@request.auth.id != \"\" && user = @request.auth.id"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("dv6hi1xylwqfrv1")

  collection.listRule = null
  collection.viewRule = null
  collection.createRule = null
  collection.updateRule = null
  collection.deleteRule = null

  return dao.saveCollection(collection)
})
