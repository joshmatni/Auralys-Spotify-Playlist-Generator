import React from 'react';
import { JsonLdProps } from './jsonld';
import type { Review, AggregateRating } from 'src/types';
export interface SoftwareAppJsonLdProps extends JsonLdProps {
    name: string;
    price: string;
    priceCurrency: string;
    applicationCategory?: string;
    operatingSystem?: string;
    review?: Review;
    aggregateRating?: AggregateRating;
    keywords?: string;
}
declare function SoftwareAppJsonLd({ type, keyOverride, priceCurrency, price, aggregateRating, review, keywords, ...rest }: SoftwareAppJsonLdProps): React.JSX.Element;
export default SoftwareAppJsonLd;
