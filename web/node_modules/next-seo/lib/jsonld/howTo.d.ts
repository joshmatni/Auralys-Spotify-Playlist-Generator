import React from 'react';
import { JsonLdProps } from './jsonld';
import { PriceSpecification, Step } from 'src/types';
export interface HowToJsonLdProps extends JsonLdProps {
    name: string;
    image?: string;
    estimatedCost?: PriceSpecification;
    supply?: string[];
    tool?: string[];
    step: Step[];
    totalTime?: string;
}
declare function howToJsonLd({ type, keyOverride, image, estimatedCost, supply, tool, step, ...rest }: HowToJsonLdProps): React.JSX.Element;
export default howToJsonLd;
