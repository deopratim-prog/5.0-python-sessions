def calculate_score(problem, demand, innovation, revenue, expertise, competition):
    score = (
        problem * 20 +
        demand * 20 +
        innovation * 15 +
        revenue * 20 +
        expertise * 15 -
        competition * 10
    )
    return score


def get_verdict(score):
    if score >= 700:
        return "INVEST READY 🚀"
    elif score >= 550:
        return "HIGH POTENTIAL 📈"
    elif score >= 400:
        return "PROMISING BUT NEEDS WORK ⚠️"
    else:
        return "HIGH RISK IDEA ❌"


print("\n" + "=" * 50)
print("      STARTUP FEASIBILITY ANALYZER")
print("=" * 50)

startup_name = input("Startup Name: ")
industry = input("Industry: ")
founder = input("Founder Name: ")

print("\nRate each parameter from 1 to 10\n")

while True:

    problem = int(input("Problem Severity: "))
    demand = int(input("Market Demand: "))
    competition = int(input("Competition Level: "))
    innovation = int(input("Innovation Factor: "))
    revenue = int(input("Revenue Potential: "))
    expertise = int(input("Founder Expertise: "))

    valid = True

    for score in [problem, demand, competition,
                  innovation, revenue, expertise]:

        if score < 1 or score > 10:
            valid = False

    if valid:
        break

    print("\nPlease enter ratings between 1 and 10.\n")

final_score = calculate_score(
    problem,
    demand,
    innovation,
    revenue,
    expertise,
    competition
)

verdict = get_verdict(final_score)

print("\n")
print("=" * 50)
print("           STARTUP REPORT")
print("=" * 50)

print("Startup :", startup_name)
print("Industry:", industry)
print("Founder :", founder)

print("\nOverall Score:", final_score)
print("Verdict:", verdict)

print("\nKey Insights")

if problem >= 8:
    print("✓ Addresses a significant real-world problem")

if demand >= 8:
    print("✓ Strong market demand detected")

if innovation >= 8:
    print("✓ Demonstrates strong innovation")

if revenue >= 8:
    print("✓ Attractive monetization potential")

if expertise >= 8:
    print("✓ Founder has relevant expertise")

if competition >= 8:
    print("⚠ Highly competitive market")

print("\nRecommendation")

if final_score >= 700:
    print("Focus on MVP development and user acquisition.")
elif final_score >= 550:
    print("Validate assumptions with real customers.")
else:
    print("Refine the idea and identify stronger opportunities.")

print("\nEnd of Report")
print("=" * 50)