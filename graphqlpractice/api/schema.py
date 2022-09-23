import graphene
from graphene_django import DjangoObjectType , DjangoListField
from .models import Post 
from .models import Category 
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery

class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()
   verify_account = mutations.VerifyAccount.Field()
   token_auth = mutations.ObtainJSONWebToken.Field()
   
class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ('id', 'title', 'category')  
        
           
class Query(UserQuery, MeQuery, graphene.ObjectType):
    # pass
        # all_category = DjangoListField(CategoryType)
    all_post = DjangoListField(PostType)
    
    # def resolve_all_category(root, info):
    #     return Post.objects.all()
    
    def resolve_all_post(root, info):
        return Post.objects.all()
        # return Post.objects.filter(id=2)

class Mutation(AuthMutation, graphene.ObjectType):
    pass

# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category
#         fields = ('id', 'name')

  
    
# class Query(graphene.ObjectType):
    
#     # all_category = DjangoListField(CategoryType)
#     all_post = DjangoListField(PostType)
    
#     # def resolve_all_category(root, info):
#     #     return Post.objects.all()
    
#     def resolve_all_post(root, info):
#         return Post.objects.all()
#         # return Post.objects.filter(id=2)
    

schema = graphene.Schema(query=Query , mutation = Mutation)