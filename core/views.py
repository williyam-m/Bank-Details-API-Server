from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bank, Branch
from django.shortcuts import redirect, render, get_object_or_404

def home(request):
  num_banks = Bank.objects.count()
  num_branches = Branch.objects.count()
  context = {'num_banks': num_banks, 'num_branches': num_branches}
  return render(request, 'home.html', context)


class BankListAPIView(APIView):

    def get(self, request):
        branch_name = request.GET.get('branch_name')
        if branch_name:
            branches = Branch.objects.filter(branch=branch_name)

        branch_data = []
        for branch in branches:
            bank = Bank.objects.get(name=branch.bank)

            branch_dict = {
                    'id': bank.id,
                    'name': bank.name,
                    'ifsc': branch.ifsc,
                    'branch': branch.branch,
                    'address': branch.address,
                    'city': branch.city,
                    'district': branch.district,
                    'state': branch.state,
            }
            branch_data.append(branch_dict)

        return Response(branch_data)

class BranchDetailAPIView(APIView):

    def get(self, request):
        ifsc_code = request.GET.get('ifsc_code')
        branch = get_object_or_404(Branch, ifsc=ifsc_code)

        return Response({
            'ifsc': branch.ifsc,
            'bank_name': branch.bank.name,
            'branch': branch.branch,
            'address': branch.address,
            'city': branch.city,
            'district': branch.district,
            'state': branch.state,
        })
