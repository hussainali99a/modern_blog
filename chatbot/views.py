# import google.generativeai as genai
# from django.conf import settings
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from blog.models import Post

# # Configure Gemini
# genai.configure(api_key=settings.GEMINI_API_KEY)

# model = genai.GenerativeModel("gemini-1.5-flash-latest")


# @csrf_exempt
# def chatbot_response(request):
#     if request.method != "POST":
#         return JsonResponse({"error": "Invalid request"}, status=400)

#     user_message = request.POST.get("message", "")

#     # Fetch recent blogs
#     blogs = Post.objects.all().order_by("-created_at")[:10]

#     blog_context = ""
#     for blog in blogs:
#         blog_context += f"""
# Title: {blog.title}
# Content: {blog.content[:1000]}
# Author: {blog.author}
# ---
# """

#     prompt = f"""
# You are an AI Blog Assistant for a Django blog website.

# Your tasks:
# 1. Help users write insightful blog posts.
# 2. Improve blog titles, intros, conclusions, SEO.
# 3. Answer questions using ONLY the blog content provided.
# 4. If answer is not found, say: "Not found in blog posts."

# Blog Data:
# {blog_context}

# User Query:
# {user_message}
# """

#     try:
#         response = model.generate_content(prompt)
#         reply = response.text
#     except Exception as e:
#         reply = f"Error: {str(e)}"

#     return JsonResponse({"reply": reply})



import google.generativeai as genai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from blog.models import Post

# Configure API
genai.configure(api_key=settings.GEMINI_API_KEY)

# ✅ Use correct model
model = genai.GenerativeModel("gemini-3-flash-preview")


@csrf_exempt
def chatbot_response(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    user_message = request.POST.get("message", "")

    # Fetch blogs
    blogs = Post.objects.all().order_by("-created_at")[:10]

    blog_context = ""
    for blog in blogs:
        blog_context += f"""
Title: {blog.title}
Content: {blog.content[:1000]}
---
"""

    prompt = f"""
You are an AI Blog Assistant.

Tasks:
- Help write blogs
- Improve content
- Answer using ONLY provided blogs
- If not found, say: Not found in blog posts

Blogs:
{blog_context}

User:
{user_message}
"""

    try:
        # ✅ IMPORTANT: use generate_content correctly
        response = model.generate_content(
            contents=[{"role": "user", "parts": [prompt]}]
        )

        reply = response.text

    except Exception as e:
        reply = f"Error: {str(e)}"

    return JsonResponse({"reply": reply})

