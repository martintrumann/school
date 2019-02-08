#include <stdio.h>

int main() {
	double kaugus, autokomp, paevaraha, majutus, parkimine, kogukulu;
	int aeg, aegh;

	printf("kaugus sihtpunktist: ");
	scanf("%lf", &kaugus);

	printf("kaua sihtpunktis viibitakse: ");
	scanf("%d", &aeg);

	aegh = aeg * 24;

	autokomp = 0.3 * kaugus;

	printf("\nauto kompensatsioon maksab %.2lf€\n", autokomp);

	if (aeg <= 15) {
		paevaraha = 15 * aeg;
	}

	if (aeg > 15) {
		paevaraha = 225 + 32 * (aeg - 15);
	}

	printf("paevaraha on %.2lf€\n", paevaraha);

	
	parkimine = 3 * aegh;

	printf("parkimine maksab %.2lf€\n", parkimine);


	majutus = 50 * (aeg - 1);

	printf("majutus maksab %.2lf€\n", majutus);


	kogukulu = autokomp + paevaraha + parkimine + majutus;

	printf("koik kulud kokku on %.2lf€\n", kogukulu);
	
	return 0;
}
