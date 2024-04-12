from enum import Enum

class UserType(Enum):
    STUDENT = 'student'
    TEACHER = 'teacher'

class ClassList(Enum):
    NURSERY = 'nursery'
    KINDERGARTEN = 'kindergarten'
    ONE = 'one'
    TWO = 'two'
    THREE = 'three'
    FOUR = 'four'
    FIVE = 'five'
    SIX = 'six'
    SEVEN = 'seven'
    EIGHT = 'eight'
    NINE = 'nine'
    TEN = 'ten'
    ELEVEN = 'eleven'
    TWELVE = 'twelve'

class SubjectList(Enum):
    ENGLISH = 'english'
    SCIENCE = 'science'
    MATHS = 'maths'
    SOCIAL = 'social'
    ARTS = 'arts'
    COMPUTER = 'computer'
    ACCOUNT = 'account'
    LANGUAGE = 'language'
    OTHERS = 'others'
    
class EducationLevel(Enum):
    MONTESSORI = 'montessori'
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    HIGHER_SECONDARY = 'higher_secondary'
    BACHELOR = 'bachelor'
    MASTER = 'master'
    PHD = 'phd'
    
class InstitutionType(Enum):
    PRIVATE = 'private'
    GOVERNMENT = 'government'
    COMMUNITY = 'community'
    INSTITUTIONAL = 'institutional'
    RELIGIOUS = 'religious'