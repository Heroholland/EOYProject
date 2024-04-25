from databasewrapper import Database
import Utils
db = Database()
util = Utils.Utility()
print(str(util.image_to_matrix("EOYProject\\testimg.jpg").get_raw()))
