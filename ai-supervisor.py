def build_supervisor_prompt(scenario, learner_response):
    return f"""
You are an expert behavioral care supervisor evaluating an early-stage neurodivergence care learner.

Evaluate the learner response against the scenario.

SCENARIO:
{scenario}

LEARNER RESPONSE:
{learner_response}

EVALUATION CRITERIA:
1. Empathy
2. Safety
3. Observation
4. Reinforcement
5. Communication
6. Practical next step
7. Documentation readiness

RETURN FORMAT:

Score:
Give a score out of 10.

Strengths:
List what the learner did well.

Growth Areas:
List what the learner missed or could improve.

Coaching Advice:
Give practical, supportive coaching.

Improved Response:
Rewrite the learner response in a stronger way.

Next Mission:
Suggest one next learning mission.
"""

if __name__ == "__main__":
    scenario = "A child refuses to transition from playtime to class and starts crying."

    learner_response = """
    I would stay calm, make sure the child feels safe,
    observe the trigger, guide them step by step, and reinforce positive behavior.
    """

    prompt = build_supervisor_prompt(scenario, learner_response)

    print(prompt)
