#include <stdio.h>
#include <math.h>

int main() {
	double pikkus, korgus, otspikkus, katusaar, katusaar2, S, hind, kulu, kutuskulu, poekaugus, kutus100, toomine, kokku;

	printf("\nmis on katuse pikkus: ");
	scanf("%lf", &pikkus);

	printf("mis on katuse harja korgus: ");
	scanf("%lf", &korgus);

	printf("mis on maja otsaseina pikkus: ");
	scanf("%lf", &otspikkus);
	
	katusaar2 =  (otspikkus / 2) + korgus;
	katusaar = sqrt(katusaar2);

	S = 2 * ( katusaar * pikkus );

	printf("\nkatuse pindala on %.2lf\n", S);

	printf("mis on ruutmeetri katuse hind: ");
	scanf("%lf", &hind);

	kulu = hind * S;

	printf("\nkatus maksab %.2lf€\n", kulu);

	printf("kui kaugel lahim ehituspood: ");
	scanf("%lf", &poekaugus);

	printf("kui palju votab auto kutust: ");
	scanf("%lf", &kutus100);

	kutuskulu = kutus100 / 100 * 1.3;
	toomine = 2 * (kutuskulu * poekaugus);

	printf("\ntoomine maksab %.2lf€\n", toomine);

	kokku = kulu + toomine;

	printf("\nkogusumma on %.2lf€\n", kokku);
}
