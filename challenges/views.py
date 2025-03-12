import csv
import os
from django.http import JsonResponse, HttpResponseServerError
from django.conf import settings

def challenge_list(request):
  csv_file_path = os.path.join(settings.BASE_DIR, 'data', 'challenges.csv')

  try:
      challenges = []
      with open(csv_file_path, 'r') as file:
          reader = csv.DictReader(file)
          for row in reader:
              challenges.append({
                  'ChallengeID': int(row['ChallengeID']),
                  'ChallengeName': row['ChallengeName'],
                  'ChallengeSuccessRate': int(row['ChallengeSucessRate']),
              })

      return JsonResponse(challenges, safe=False)

  except FileNotFoundError:
      return JsonResponse({'error': 'CSV file not found'}, status=404)
  except Exception as e:
      return JsonResponse({'error': str(e)}, status=500)