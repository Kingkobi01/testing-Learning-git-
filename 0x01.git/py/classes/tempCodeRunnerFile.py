def __repr__(self):
      description = ""
      for country in self.catalogue:
        description += f"{str(country)}\n"
      
      return description
