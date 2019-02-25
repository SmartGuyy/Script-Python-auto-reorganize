
#fonction pour supprimer une valeur d'une liste

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]