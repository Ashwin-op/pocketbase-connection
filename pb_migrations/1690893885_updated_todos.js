migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("dv6hi1xylwqfrv1")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "cmxmhewz",
    "name": "user",
    "type": "relation",
    "required": true,
    "unique": false,
    "options": {
      "collectionId": "_pb_users_auth_",
      "cascadeDelete": true,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": []
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("dv6hi1xylwqfrv1")

  // remove
  collection.schema.removeField("cmxmhewz")

  return dao.saveCollection(collection)
})
