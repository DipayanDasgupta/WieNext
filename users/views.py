from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from .forms import OnboardingForm
from .ai_onboarding import evaluate_user_level
from django.shortcuts import render, redirect

def onboarding_view(request):
    if request.method == "POST":
        form = OnboardingForm(request.POST)
        if form.is_valid():
            # Use LangChain to analyze responses
            template = PromptTemplate(
                input_variables=["responses"],
                template="Given the following responses: {responses}, categorize the user as Beginner, Intermediate, or Advanced."
            )
            chain = LLMChain(llm=LangChain(), prompt=template)
            user_level = chain.run(responses=form.cleaned_data)
            
            request.user.level = user_level
            request.user.save()
            return redirect('dashboard')
    else:
        form = OnboardingForm()
    return render(request, 'onboarding.html', {'form': form})
