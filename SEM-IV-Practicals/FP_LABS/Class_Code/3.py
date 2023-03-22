class Sample:
    a = "GUNI-ICT"

object = Sample()
object.a = "UPVCE"
Sample.a = "Updated_GUNI-ICT"

print(object.a)
print(Sample.a)