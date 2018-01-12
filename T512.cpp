#include <cstdio>

int flag[250000005];
int phi[250000005];
int primenum;
int prime[250000005];

int main()
{
	long long ans = 0;
	phi[1] = 1;
	for (int i = 2; i <= 500000000; i++)
	{
		if (i & 1)
		{
			if (! flag[(i + 1) / 2])
			{
				primenum++;
				prime[primenum] = i;
				phi[(i + 1) / 2] = i - 1;
			}
			for (int j = 1; j <= primenum && i * prime[j] <= 500000000; j++)
			{
				flag[(i * prime[j] + 1) / 2] = 1;
				if (i % prime[j] == 0)
				{
					phi[(i * prime[j] + 1) / 2] = phi[(i + 1) / 2] * prime[j];
					break;
				}
				phi[(i * prime[j] + 1) / 2] = phi[(i + 1) / 2] * (prime[j] - 1);
			}
		}
	}
	for (int i = 1; i <= 250000000; i++)
	{
		ans += phi[i];
	}
	printf("%lld\n", ans);
	return 0;
}
