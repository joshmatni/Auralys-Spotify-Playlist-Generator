import React from 'react';
import type { Question } from 'src/types';
import { JsonLdProps } from './jsonld';
export interface FAQPageJsonLdProps extends JsonLdProps {
    mainEntity: Question[];
}
declare function FAQPageJsonLd({ type, keyOverride, mainEntity, ...rest }: FAQPageJsonLdProps): React.JSX.Element;
export default FAQPageJsonLd;
