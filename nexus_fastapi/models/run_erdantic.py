import erdantic as erd
#from erdantic.examples.pydantic import Party
from ..models import User

# Easy one-liner
erd.draw(User, out="User.png")

# Or create a diagram object that you can inspect and do stuff with
#diagram = erd.create(Party)
#list(diagram.models.keys())
#> [ 'erdantic.examples.pydantic.Adventurer',
#>   'erdantic.examples.pydantic.Party',
#>   'erdantic.examples.pydantic.Quest',
#>   'erdantic.examples.pydantic.QuestGiver']
#diagram.draw("diagram.png")
