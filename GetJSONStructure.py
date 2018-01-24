"""
Question: Given Json data, return the structure of it 
"""
class GetStructure(object):
      def __init__(self):
            self.stack = list()

      def get_structure(self, data, class_name):
            result = ""
            for tclass_name, value in data.iteritems():
                  if type(value) in [int, str, float]:
                        result += "\t %s : %s\n" % (tclass_name, type(value))

                  elif type(value) == list:
                        result += "\t %s: %s\n" % (tclass_name, self.helper(value, tclass_name))

                  else:
                        result += "\t %s: %s\n" % (tclass_name, tclass_name.title())
                        self.get_structure(value, tclass_name)

            result = "Class %s: \n" % class_name.title() + result
            print result
                              

      def helper(self, data, class_name):
            item = data[-1]
            if type(item) in [int, float, str]:
                  return "List(%s)" % type(item)

            elif type(item) == list:
                  return "List(%s)" % self.helper(item, class_name)

            else:
                  self.get_structure(item, class_name)
                  return "List(%s)" % class_name.title()
                  
                  

data = {
	"squadName": "Super hero squad",
	"homeTown": "Metro City",
	"formed": 2016,
	"members": [{
			"name": "Madame Uppercut",
			"age": 39,
			"secretIdentity": "Jane Wilson",
			"powers": [
				"Million tonne punch",
				"Damage resistance",
				"Superhuman reflexes"
			]
		},
		{
			"name": "Eternal Flame",
			"age": 1000000,
			"secretIdentity": "Unknown",
			"powers": [
				"Immortality",
				"Heat Immunity",
				"Inferno",
				"Teleportation",
				"Interdimensional travel"
			]
		}
	],

        "Random" : {
			"name": "Eternal Flame",
			"age": 1000000,
			"secretIdentity": "Unknown",
			"powers": {
                              "name": "Eternal Flame",
                              "age": 1000000,
                              "secretIdentity": "Unknown",
                              "powers": [
                                      "Immortality",
                                      "Heat Immunity",
                                      "Inferno",
                                      "Teleportation",
                                      "Interdimensional travel"
			         ]
		        }
		}
}

class_name = "order"                 

gs = GetStructure()
gs.get_structure(data, class_name)



"""
Ouput

Class Powers: 
	 powers: List(<type 'str'>)
	 age : <type 'int'>
	 secretIdentity : <type 'str'>
	 name : <type 'str'>

Class Random: 
	 powers: Powers
	 age : <type 'int'>
	 secretIdentity : <type 'str'>
	 name : <type 'str'>

Class Members: 
	 powers: List(<type 'str'>)
	 age : <type 'int'>
	 secretIdentity : <type 'str'>
	 name : <type 'str'>

Class Order: 
	 homeTown : <type 'str'>
	 squadName : <type 'str'>
	 formed : <type 'int'>
	 Random: Random
	 members: List(Members)
"""

                  
                  
